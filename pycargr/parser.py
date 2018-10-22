#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = 'Florents Tselai'

from datetime import datetime
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from .db import RedisCache
from .model import Car, to_dict


class SearchResultPageParser:
    def __init__(self, search_page_url):
        self.search_page_url = search_page_url
        req = Request(
            search_page_url,
            data=None,
            headers={
                'User-Agent': UserAgent().chrome
            }
        )
        self.html = urlopen(req).read().decode('utf-8')
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.num_results = None
        for f in self.soup.find_all('strong'):
            if 'αγγελίες' in f.text:
                if f.text.split()[0].isdigit():
                    self.num_results = int(f.text.split()[0])

    def parse(self):
        car_ids = []
        for a in self.soup.find_all('a', class_='vehicle list-group-item clsfd_list_row'):
            car_ids.append(int(a.get('href').replace('/', '').split('-')[0]))
        return car_ids


class CarItemParser:
    def __init__(self, car_id):
        self.car_id = car_id
        self.req = Request(
            'https://www.car.gr/%s' % self.car_id,
            data=None,
            headers={
                'User-Agent': UserAgent().chrome
            }
        )
        self.html = urlopen(self.req).read().decode('utf-8')
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def parse_km(self):
        try:
            for td in self.soup.find_all('td'):
                if 'χμ' in td.text:
                    return float(td.text.replace('.', '').replace('χμ', ''))
        except Exception:
            return None
        return None

    def parse_bhp(self):
        try:
            for td in self.soup.find_all('td'):
                if 'bhp' in td.text:
                    return int(td.text.replace(' bhp', ''))
        except Exception:
            return None
        return None

    def parse_title(self):
        try:
            return self.soup.find('title').text
        except Exception:
            return None

    def parse_price(self):
        try:
            return float(self.soup.find(itemprop='price').text.replace('.', '').replace('€ ', ''))
        except Exception:
            return None

    def parse_release_date(self):
        try:
            date_str = self.soup.find(itemprop='releaseDate').text.strip()
            return datetime.strptime(date_str, "%m / %Y").strftime("%b %Y")
        except Exception:
            return None

    def parse_engine(self):
        try:
            return int(self.soup.find(id='clsfd_engine_%s' % self.car_id).text.replace(' cc', '').replace('.', ''))
        except Exception:
            return None

    def parse_color(self):
        try:
            return self.soup.find(itemprop='color').text
        except Exception:
            return None

    def parse_fueltype(self):
        try:
            return self.soup.find(id='clsfd_fueltype_%s' % self.car_id).text
        except Exception:
            return None

    def parse_description(self):
        try:
            return self.soup.find(itemprop='description').text
        except Exception:
            return None

    def parse_city(self):
        try:
            return self.soup.find('span', itemprop='addressLocality').text
        except Exception:
            return None

    def parse_region(self):
        try:
            return self.soup.find('span', itemprop='addressRegion').text

        except Exception:
            return None

    def parse_postal_code(self):
        try:
            return int(self.soup.find('span', itemprop='postalCode').text)

        except Exception:
            return None

    def parse_transmission(self):
        try:
            return self.soup.find(id='clsfd_transmision_%s' % self.car_id).text
        except Exception:
            return None

    def parse_images(self):
        try:
            images_urls = []
            for img in self.soup.find_all('img', itemprop='image'):
                images_urls.append(img.get('src').replace(r'//', 'https://').replace('_v', '_b'))
            return images_urls
        except Exception:
            return None

    def parse(self):
        c = Car(self.car_id)
        c.title = self.parse_title()
        c.price = self.parse_price()
        c.release_date = self.parse_release_date()
        c.engine = self.parse_engine()
        c.km = self.parse_km()
        c.bhp = self.parse_bhp()
        c.url = self.req.full_url
        c.color = self.parse_color()
        c.fueltype = self.parse_fueltype()
        c.description = self.parse_description()
        c.city = self.parse_city()
        c.region = self.parse_region()
        c.postal_code = self.parse_postal_code()
        c.transmission = self.parse_transmission()
        c.images = self.parse_images()

        return c


def parse_search_results(search_url):
    car_ids = SearchResultPageParser(search_url).parse()
    results = []
    for car_id in car_ids:
        car_data = parse_car_page(car_id)
        results.append(car_data)
    return results


def parse_car_page(car_id):
    car = CarItemParser(car_id).parse()
    return to_dict(car)
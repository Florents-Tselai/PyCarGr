#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = 'Florents Tselai'


class Car:
    def __init__(self, car_id):
        self._car_id = car_id

    @property
    def car_id(self):
        return self._car_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        self._release_date = release_date

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def url(self):
        return 'http://car.gr/{}'.format(self._car_id)

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def km(self):
        return self._km

    @km.setter
    def km(self, km):
        self._km = km

    @property
    def bhp(self):
        return self._bhp

    @bhp.setter
    def bhp(self, bhp):
        self._bhp = bhp

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def fueltype(self):
        return self._fueltype

    @fueltype.setter
    def fueltype(self, fueltype):
        self._fueltype = fueltype

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, transmission):
        self._transmission = transmission

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, images):
        self._images = images

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, html):
        self._html = html

    @property
    def scraped_at(self):
        return self._scraped_at

    @scraped_at.setter
    def scraped_at(self, scraped_at):
        self._scraped_at = scraped_at


def to_dict(model):
    return dict((get_key(key), value)
                for key, value in model.__dict__.items()
                if not callable(value) and not key.startswith("__"))


def get_key(key):
    return key.replace("_", "", 1) if key.startswith("_") else key

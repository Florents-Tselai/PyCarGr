from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

from pycargr import save_car
from pycargr.parser import parse_search_results

SEARCH_URL = "https://www.car.gr/classifieds/cars/?fs=1&condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale"
MAX_PAGES = 10 ** 4
MAX_WORKERS = 10


def work_page_id(page_url):
    for c in parse_search_results(page_url):
        save_car(c)


def main():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        fts = []
        for page in range(1, MAX_PAGES):
            fts.append(executor.submit(work_page_id, SEARCH_URL + '&pg=%d' % page))

        for _ in tqdm(as_completed(fts), total=MAX_PAGES, unit='page'):
            pass


if __name__ == '__main__':
    main()

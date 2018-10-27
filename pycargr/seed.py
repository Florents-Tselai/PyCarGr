from concurrent.futures import ThreadPoolExecutor, as_completed
from sqlite3 import connect

from tqdm import tqdm

from pycargr import DB_PATH
from pycargr import save_car
from pycargr.parser import SearchResultPageParser, CarItemParser

SEARCH_URL = "https://www.car.gr/classifieds/cars/?fs=1&offer_type=sale&sort=rea"
MAX_PAGES = 10 ** 4
MAX_WORKERS = 10


def work_car_id(cid):
    save_car(CarItemParser(cid).parse())


def work_search_page(search_page_url):
    with ThreadPoolExecutor(max_workers=15) as executor:
        search_page_parser = SearchResultPageParser(search_page_url)
        for cid in search_page_parser.parse():
            is_saved = False
            with connect(str(DB_PATH)) as db:
                is_saved = int(db.execute("SELECT count(*) FROM cars WHERE id=?", (cid,)).fetchone()[0]) > 0
            if not is_saved:
                executor.submit(work_car_id, cid)
            else:
                pass


def main():
    with ThreadPoolExecutor(max_workers=200) as executor:
        fts = []
        for search_page_url in [SEARCH_URL + '&pg=%d' % page for page in range(1, MAX_PAGES)]:
            fts.append(executor.submit(work_search_page, search_page_url))

        list(tqdm(as_completed(fts), desc='Scraping pages', unit='page', total=MAX_PAGES))


if __name__ == '__main__':
    main()

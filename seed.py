from sqlite3 import connect

from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from pycargr import save_car, DB_PATH
from pycargr.parser import parse_search_results, SearchResultPageParser, CarItemParser

SEARCH_URL = "https://www.car.gr/classifieds/cars/?fs=1&offer_type=sale&sort=rea"
MAX_PAGES = 10 ** 4
MAX_WORKERS = 50


def work_car_id(cid):
    save_car(CarItemParser(cid).parse())


def main():
    not_saved = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        for search_page_url in tqdm([SEARCH_URL + '&pg=%d' % page for page in range(1, MAX_PAGES)]):
            search_page_parser = SearchResultPageParser(search_page_url)
            for cid in search_page_parser.parse():
                is_saved = False
                with connect(str(DB_PATH)) as db:
                    is_saved = int(db.execute("SELECT count(*) FROM cars WHERE id=?", (cid,)).fetchone()[0]) > 0
                if not is_saved:
                    #save_car(CarItemParser(cid).parse())
                    #not_saved.append(cid)
                    executor.submit(work_car_id, cid)

                else:
                    pass
                    #print(f"{cid} is already saved")


if __name__ == '__main__':
    main()

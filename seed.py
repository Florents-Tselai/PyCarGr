from pycargr.parser import parse_search_results
from pycargr import save_car
from tqdm import tqdm
SEARCH_URL = "https://www.car.gr/classifieds/cars/?fs=1&condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale"


def main():
    for c in tqdm(parse_search_results(SEARCH_URL)):
        save_car(c)

if __name__ == '__main__':
    main()

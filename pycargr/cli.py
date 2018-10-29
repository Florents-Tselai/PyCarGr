import csv
from argparse import ArgumentParser
from json import dumps

from pycargr.model import to_dict
from pycargr.parser import parse_car_page

parser = ArgumentParser(description='CLI interface to interact with car.gr')
parser.add_argument('car_ids', nargs='+')
parser.add_argument('--output', choices=['csv', 'json', 'stdout'], default='stdout')
parser.add_argument('--scrape',
                    help='If set scraps the page again and replace the DB entry. Otherwise atempts to read from already-scraped version',
                    default=True)


def main():
    args = parser.parse_args()
    car_ids = args.car_ids
    output = args.output
    scrape = args.scrape

    results = []
    for cid in car_ids:
        if scrape:
            c_data = to_dict(parse_car_page(cid))
        else:
            # TODO: Fetch from DB
            raise NotImplementedError
        c_data.pop('html')
        results.append(c_data)

    if output == 'csv':
        with open('data.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            for d in results:
                # images is a list - not suitable for csv
                d.pop('images')
                d.pop('html')
                writer.writerow(d)
    elif output == 'json' or output == 'stdout':
        print(dumps(results, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()

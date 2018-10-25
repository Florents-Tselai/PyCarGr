import csv
from argparse import ArgumentParser
from json import dumps

from pycargr.model import to_dict
from pycargr.parser import parse_car_page

parser = ArgumentParser()
parser.add_argument('car_ids', nargs='+')
parser.add_argument('--output', choices=['csv', 'json', 'stdout'], default='stdout')


def main():
    args = parser.parse_args()
    car_ids = args.car_ids
    output = args.output

    results = []
    for cid in car_ids:
        results.append(to_dict(parse_car_page(cid)))

    if output == 'csv':
        with open('data.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            for d in results:
                # images is a list - not suitable for csv
                d.pop('images')
                writer.writerow(d)
    elif output == 'stdout':
    print(dumps(results, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()

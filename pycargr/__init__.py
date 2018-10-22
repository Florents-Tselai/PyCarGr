from json import dumps
from pathlib import Path
from sqlite3 import connect

from pycargr.model import Car

DB_PATH = Path.home().joinpath('pycargr.db')


def save_car(*cars):
    assert all(isinstance(c, Car) for c in cars)
    with connect(str(DB_PATH), timeout=10) as db:
        db.executemany("INSERT OR REPLACE INTO cars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       [(c.car_id, c.title, c.price, c.release_date, c.km, c.bhp, c.url, c.color, c.fueltype,
                         c.description, c.city, c.region, c.postal_code, c.transmission, dumps(c.images), c.html,
                         c.scraped_at) for c in
                        cars])

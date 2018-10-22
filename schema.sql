CREATE TABLE IF NOT EXISTS cars
(
  id           TEXT PRIMARY KEY,
  title        TEXT,
  price        REAL,
  release_date TEXT,
  km           REAL,
  bhp          INT,
  url          TEXT,
  color        TEXT,
  fueltype     TEXT,
  description  TEXT,
  city         TEXT,
  region       TEXT,
  postal_code  TEXT,
  transmission TEXT,
  images       TEXT, -- JSON LIST,
  raw_html     TEXT,
  scraped_at   TEXT
);

CREATE INDEX IF NOT EXISTS idx_cars_color ON cars(color);
CREATE INDEX IF NOT EXISTS idx_cars_fueltype ON cars(fueltype);
CREATE TABLE IF NOT EXISTS cars(
  id TEXT PRIMARY KEY,
  title TEXT,
  price REAL,
  release_date TEXT,
  km REAL,
  bhp INT,
  url TEXT,
  color TEXT,
  fueltype TEXT,
  description TEXT,
  city TEXT,
  region TEXT,
  postal_code TEXT,
  transmission TEXT,
  images TEXT, -- JSON LIST,
  raw_html TEXT
);
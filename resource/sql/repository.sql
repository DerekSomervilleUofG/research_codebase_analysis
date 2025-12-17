CREATE TABLE IF NOT EXISTS repository(
    repository_id INTEGER PRIMARY KEY,
    name TEXT,
    url TEXT NOT NULL UNIQUE,
    packages TEXT

)
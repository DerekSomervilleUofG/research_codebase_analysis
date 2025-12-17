CREATE TABLE IF NOT EXISTS file(
    file_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    repository_id INTEGER,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)

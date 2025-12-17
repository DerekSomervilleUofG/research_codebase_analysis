CREATE TABLE IF NOT EXISTS class(
    class_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    file_id INTEGER NOT NULL,
    repository_id INTEGER NOT NULL,
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)

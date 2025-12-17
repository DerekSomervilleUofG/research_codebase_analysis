    CREATE TABLE IF NOT EXISTS method(
    method_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    class_id INTEGER NOT NULL,
    repository_id INTEGER NOT NULL,
    FOREIGN KEY(class_id) REFERENCES class(class_id),
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)

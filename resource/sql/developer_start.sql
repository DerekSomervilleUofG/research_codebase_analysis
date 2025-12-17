CREATE TABLE IF NOT EXISTS developer_start(
    developer_start_id INTEGER PRIMARY KEY autoincrement,
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id),
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
)
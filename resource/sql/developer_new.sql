CREATE TABLE IF NOT EXISTS developer_new(
    developer_new_id INTEGER PRIMARY KEY autoincrement,
    number_of_commits INTEGER,
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id),
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
)
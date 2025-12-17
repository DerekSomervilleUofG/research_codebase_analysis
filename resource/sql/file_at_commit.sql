CREATE TABLE IF NOT EXISTS file_at_commit(
    commit_id TEXT,
    path TEXT,
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id),
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
)
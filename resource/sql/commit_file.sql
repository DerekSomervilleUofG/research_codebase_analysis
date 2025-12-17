CREATE TABLE IF NOT EXISTS commit_file(
    commit_file_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    amendment_type TEXT,
    file_id INTEGER NOT NULL,
    commit_id TEXT NOT NULL,
    repository_id INTEGER NOT NULL,
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id),
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)

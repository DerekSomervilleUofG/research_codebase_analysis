CREATE TABLE IF NOT EXISTS commit_class(
    commit_class_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    amendment_type TEXT,
    class_id INTEGER,
    file_id INTEGER NOT NULL,
    commit_id TEXT,
    repository_id INTEGER NOT NULL,
    FOREIGN KEY(class_id) REFERENCES class(class_id),
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id),
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)

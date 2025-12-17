CREATE TABLE IF NOT EXISTS amend_commit(
    commit_id TEXT PRIMARY KEY,
    packages TEXT,
    total_number_of_known_files INTEGER,
    total_number_of_known_classes INTEGER,
    total_number_of_known_methods INTEGER,
    number_of_amend_files INTEGER,
    number_of_amend_classes INTEGER,
    number_of_amend_methods INTEGER,     
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id),
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
   )

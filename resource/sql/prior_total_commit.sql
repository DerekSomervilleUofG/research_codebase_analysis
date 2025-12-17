CREATE TABLE IF NOT EXISTS prior_total_commit(
    commit_id TEXT PRIMARY KEY,
    number_of_known_files INTEGER,
    number_of_known_classes INTEGER,
    number_of_known_methods INTEGER,    
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id),
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
   )

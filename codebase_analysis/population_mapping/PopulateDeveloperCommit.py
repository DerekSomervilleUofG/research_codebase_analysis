from repository_save.population_mapping.PopulateDeveloperCommit import PopulateDeveloperCommit as SupperClass

class PopulateDeveloperCommit(SupperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns += ", number_of_repo_files, number_of_repo_classes, number_of_repo_methods "
            
    def select_commit_size (self, developer_id, end_date):
        select_statement = "select dc.commit_id, dc.authored_date, number_of_repo_files, number_of_repo_classes, number_of_repo_methods "
        select_statement += "from developer_commit dc "
        select_statement += " where dc.developer_id = " + str(developer_id)
        select_statement += " AND dc.authored_date < " + str(end_date)
        select_statement += " order by dc.authored_date asc "
        return select_statement
    
    def prepare_batch_select(self, developer_id, end_date):
        return self.db_execute_sql.prepare_batch_select(self.select_commit_size(developer_id, end_date))

    def generate_row(self, developer_commit):
        row = super().generate_row(developer_commit)
        row.append(developer_commit.repo_file_count)
        row.append(developer_commit.repo_class_count)
        row.append(developer_commit.repo_method_count)
        return row
    
            
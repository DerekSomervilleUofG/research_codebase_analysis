from repository_save.population_mapping.PopulateCommitFile import PopulateCommitFile as SuperClass

class PopulateCommitFile(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns = " name, amendment_type, file_id, commit_id, repository_id "
        
    def select_commit_file(self, developer_id, end_date ):
        select_statement = " SELECT cf.file_id, cf.commit_id, f.name, cf.amendment_type "
        select_statement += " FROM commit_file cf, developer_commit dc, file f "
        select_statement += " WHERE dc.developer_id = " + str(developer_id) 
        select_statement += " AND cf.commit_id = dc.commit_id "
        select_statement += " AND cf.file_id = f.file_id "
        select_statement += " AND dc.authored_date < " + str(end_date)
        select_statement += " order by dc.authored_date " 
        return select_statement
        
    def prepare_batch_select(self, developer_id, min_start):
        return self.db_execute_sql.prepare_batch_select(self.select_commit_file(developer_id, min_start))
    
    def generate_row(self, commit_file):
        return [commit_file.file.name, commit_file.amendment_type, commit_file.file.get_primary_key(), commit_file.commit_id, commit_file.repository.get_primary_key()]
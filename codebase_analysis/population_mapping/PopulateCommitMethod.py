from repository_save.population_mapping.PopulateCommitMethod import PopulateCommitMethod as SuperClass

class PopulateCommitMethod(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns = "name, amendment_type, method_id, class_id, commit_id, repository_id"
        
    def select_commit_method(self, developer_id, end_date ):
        select_statement = " SELECT cm.method_id, cm.commit_id, f.name || '&' || c.name || '&' || m.name, cm.amendment_type "
        select_statement += " FROM commit_method cm, developer_commit dc, method m, class c, file f "
        select_statement += " WHERE dc.developer_id = " + str(developer_id) 
        select_statement += " AND cm.commit_id = dc.commit_id "
        select_statement += " AND cm.method_id = m.method_id "
        select_statement += " AND m.class_id = c.class_id "
        select_statement += " AND c.file_id = f.file_id "
        select_statement += " AND dc.authored_date < " + str(end_date)
        select_statement += " order by dc.authored_date " 
        return select_statement
        
    def prepare_batch_select(self, developer_id, min_start):
        return self.db_execute_sql.prepare_batch_select(self.select_commit_method(developer_id, min_start))
    
    def generate_row(self, commit_method):
        return [commit_method.method.name, commit_method.amendment_type, commit_method.method.get_primary_key(), commit_method.method.class_structure.get_primary_key(), commit_method.commit_id, commit_method.repository.get_primary_key()]
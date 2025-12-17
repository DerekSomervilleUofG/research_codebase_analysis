from repository_save.population_mapping.PopulateCommitClass import PopulateCommitClass as SuperClass

class PopulateCommitClass(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns = "name, amendment_type, class_id, file_id, commit_id, repository_id"
        
    def select_commit_class(self, developer_id, end_date ):
        select_statement = " SELECT cc.class_id, cc.commit_id, f.name || '&' || c.name, cc.amendment_type "
        select_statement += " FROM commit_class cc, developer_commit dc, class c, file f "
        select_statement += " WHERE dc.developer_id = " + str(developer_id) 
        select_statement += " AND cc.commit_id = dc.commit_id "        
        select_statement += " AND cc.class_id = c.class_id "
        select_statement += " AND c.file_id = f.file_id "
        select_statement += " AND dc.authored_date < " + str(end_date)
        select_statement += " order by dc.authored_date " 
        return select_statement
        
    def prepare_batch_select(self, developer_id, min_start):
        return self.db_execute_sql.prepare_batch_select(self.select_commit_class(developer_id, min_start))
    
    def generate_row(self, commit_class_structure):
        return [commit_class_structure.class_structure.name, commit_class_structure.amendment_type, commit_class_structure.class_structure.get_primary_key(), commit_class_structure.class_structure.file.get_primary_key(), commit_class_structure.commit_id, commit_class_structure.repository.get_primary_key()]
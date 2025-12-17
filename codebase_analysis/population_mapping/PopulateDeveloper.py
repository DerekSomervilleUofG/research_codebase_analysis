from repository_save.population_mapping.PopulateDeveloper import PopulateDeveloper as SuperClass

class PopulateDeveloper(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        
    def select_developer(self):
        select_statement = " SELECT d.developer_id, d.name, d.email, d.login, 0 "
        select_statement += " FROM developer d"
        return select_statement
    
    def select_developer_with_start_date(self):
        select_statement = " SELECT d.developer_id, d.name, d.email, d.login, min(dc.authored_date), count(dc.commit_id) "
        select_statement += " FROM developer d, developer_commit dc "
        select_statement += " WHERE d.developer_id = dc.developer_id "
        select_statement += " GROUP BY d.developer_id "
        return select_statement
        
    def prepare_batch_select_with_start_date(self):
        return self.db_execute_sql.prepare_batch_select(self.select_developer_with_start_date())

    def prepare_batch_select(self):
        return self.db_execute_sql.prepare_batch_select(self.select_developer())

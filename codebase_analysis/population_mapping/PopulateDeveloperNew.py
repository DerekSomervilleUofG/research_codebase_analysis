from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateDeveloperNew(PopulateStructure):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "developer_new"
        self.all_columns = "developer_new_id, number_of_commits, developer_id, repository_id"
        self.primary_key = "developer_new_id"
        
    def generate_row(self, developer_new):
        return [developer_new.number_of_commits, developer_new.developer.get_primary_key(), developer_new.repository.get_primary_key()]
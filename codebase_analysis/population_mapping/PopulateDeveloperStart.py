from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateDeveloperStart(PopulateStructure):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "developer_start"
        self.all_columns = "developer_start_id, developer_id, repository_id"
        self.primary_key = "developer_start_id"
        
    def generate_row(self, developer_start):
        return [developer_start.developer.get_primary_key(), developer_start.repository.get_primary_key()]
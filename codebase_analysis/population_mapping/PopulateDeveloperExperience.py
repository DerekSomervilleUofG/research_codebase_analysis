from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateDeveloperExperience(PopulateStructure):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "developer_experience"
        self.all_columns = "developer_experience_id, score, developer_id"
        self.primary_key = "developer_experience_id"

    def generate_row(self, structure):
        row = []
        row.append(structure.get_code())
        row.append(structure.get_score())
        return row
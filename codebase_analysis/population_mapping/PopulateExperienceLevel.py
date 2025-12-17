from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateExperienceLevel(PopulateStructure):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "experience_level"
        self.all_columns = "experience_level_id, code, score"
        self.primary_key = "experience_level_id"

    def generate_row(self, structure):
        row = []
        row.append(structure.get_code())
        row.append(structure.get_score())
        return row
    
    def populate_structure_id(self, structures, structure_id, structure_dict):
        pass
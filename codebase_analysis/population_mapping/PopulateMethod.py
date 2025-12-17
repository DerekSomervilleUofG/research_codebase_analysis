from repository_save.population_mapping.PopulateMethod import PopulateMethod as SuperClass

class PopulateMethod(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns += ", repository_id "
        
    def generate_row(self, method):
        row = super().generate_row(method)
        row.append(method.repository.get_primary_key())
        return row
from repository_save.population_mapping.PopulateRepository import PopulateRepository as SuperClass

class PopulateRepository(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns += " , packages "
        
    def generate_row(self, repository):
        row = super().generate_row(repository)
        row.append(str(repository.packages))
        return row
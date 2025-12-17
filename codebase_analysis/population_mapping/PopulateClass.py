from repository_save.population_mapping.PopulateClass import PopulateClass as SuperClass

class PopulateClass(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns += ", repository_id"
    
    def prepare_batch_select(self, repository_id):
        select_statement = self.generate_select_record(self.table_name, self.all_columns)
        select_statement += " WHERE repository_id = " + str(repository_id)
        return self.db_execute_sql.prepare_batch_select(select_statement)
    
    def generate_row(self, class_used):
        row = super().generate_row(class_used)
        row.append(class_used.repository.get_primary_key())
        return row

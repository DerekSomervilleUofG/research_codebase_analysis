from repository_save.population_mapping.PopulateFile import PopulateFile as SuperClass

class PopulateFile(SuperClass):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.all_columns = "file_id, name, repository_id "
    
    def prepare_batch_select(self, repository_id):
        select_statement = self.generate_select_record(self.table_name, self.all_columns)
        select_statement += " WHERE repository_id = " + str(repository_id)
        return self.db_execute_sql.prepare_batch_select(select_statement)

    def generate_row(self, file):
        return [file.name, file.repository.get_primary_key()]
from repository_save.population_mapping.PopulateStructureIndividual import PopulateStructureIndividual
from utility.UtilityText import UtilityText

class PopulateFileAtCommit(PopulateStructureIndividual):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "file_at_commit"
        self.all_columns = "commit_id, path, developer_id, repository_id"
        self.primary_key = "commit_id"
        
    def populate_structure_id(self, structures, structure_id, structure_dict):
        pass
    
    def generate_row(self, file_at_commit):
        return [UtilityText.formate_text(file_at_commit.get_name()), file_at_commit.path, file_at_commit.get_developer_id(), file_at_commit.get_repository_id() ]
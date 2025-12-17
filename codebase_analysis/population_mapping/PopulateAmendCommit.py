from repository_save.population_mapping.PopulateStructureIndividual import PopulateStructureIndividual
from utility.UtilityText import UtilityText

class PopulateAmendCommit(PopulateStructureIndividual):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "amend_commit"
        self.all_columns = "commit_id, packages, total_number_of_known_files, total_number_of_known_classes, total_number_of_known_methods, number_of_amend_files, number_of_amend_classes, number_of_amend_methods, developer_id, repository_id "
        self.primary_key = ""

    def generate_row(self, amend_commit):
        return [UtilityText.formate_text(amend_commit.get_name()), amend_commit.packages, amend_commit.total_file_count, amend_commit.total_class_count, amend_commit.total_method_count, amend_commit.no_of_files, amend_commit.no_of_classes, amend_commit.no_of_methods, amend_commit.get_developer_id(), amend_commit.get_repository_id() ]
    
    def populate_structure_id(self, structures, structure_id, structure_dict):
        pass
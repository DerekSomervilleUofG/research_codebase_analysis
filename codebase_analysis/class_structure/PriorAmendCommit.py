from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class PriorAmendCommit(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, commit_id, no_of_files, no_of_classes, no_of_methods, developer, repository) -> None:
        super().__init__(commit_id)
        self.no_of_files = no_of_files
        self.no_of_classes = no_of_classes
        self.no_of_methods = no_of_methods
        self.repository = repository
        self.developer = developer
        self.populate_structure = self.control_populate.get_populate_prior_amend_commit()
        self.populate_structure.add_structure(self)
        
    def get_developer_id(self):
        return self.developer.get_primary_key()
    
    def get_repository_id(self):
        return self.repository.get_primary_key()
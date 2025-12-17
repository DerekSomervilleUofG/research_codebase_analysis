from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class AmendCommit(Structure):
    
    control_populate = LocalControlPopulate()
    
    def __init__(self, commit_id, packages, total_file_count, total_class_count, total_method_count, file_count, class_count, method_count, developer, repository):
        super().__init__(commit_id)
        self.commit_id = commit_id
        self.packages = packages
        self.no_of_files = file_count
        self.no_of_classes = class_count
        self.no_of_methods = method_count
        self.total_file_count = total_file_count
        self.total_class_count = total_class_count
        self.total_method_count = total_method_count
        self.developer = developer
        self.repository = repository
        self.populate_structure = self.control_populate.get_populate_amend_commit()
        self.populate_structure.add_structure(self)
        pass
    
    def get_developer_id(self):
        return self.developer.get_primary_key()
    
    def get_repository_id(self):
        return self.repository.get_primary_key()
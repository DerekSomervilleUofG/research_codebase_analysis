from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class DeveloperNew(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, developer, repository, number_of_commits) -> None:
        super().__init__(developer.name)
        self.repository = repository
        self.developer = developer
        self.number_of_commits = number_of_commits
        self.populate_structure = self.control_populate.get_populate_developer_new()
        self.populate_structure.add_structure(self)
   
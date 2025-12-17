from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class DeveloperStart(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, developer, repository) -> None:
        super().__init__(developer.name)
        self.repository = repository
        self.developer = developer
        self.populate_structure = self.control_populate.get_populate_developer_start()
        self.populate_structure.add_structure(self)
   
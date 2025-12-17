from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class Method(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, name, class_structure, repository) -> None:
        super().__init__(name)
        self.class_structure = class_structure
        self.owned_by_class = class_structure
        self.repository = repository
        self.populate_structure = self.control_populate.get_populate_method()
        self.populate_structure.add_structure(self)
     
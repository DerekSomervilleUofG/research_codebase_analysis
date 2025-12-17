from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class ClassStructure(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, name, file, repository) -> None:
        super().__init__(name)
        self.methods = []
        self.file = file
        self.repository = repository
        self.owned_by_file = file
        self.populate_structure = self.control_populate.get_populate_class()
        self.populate_structure.add_structure(self)
     
    def add_method(self, method):
        self.methods.append(method)
        
    def delete_methods(self):
        self.methods = []
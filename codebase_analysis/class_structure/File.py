from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class File(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, name, repository) -> None:
        super().__init__(name)
        self.classes = []
        self.repository = repository
        self.populate_structure = self.control_populate.get_populate_file()
        self.populate_structure.add_structure(self)
     
    def get_file_id(self):
        return self.get_primary_key()
    
    def add_class(self, class_structure):
        self.classes.append(class_structure)
        
    def delete_classes(self):
        for class_structure in self.classes:
            class_structure.delete_methods()
        self.classes = []
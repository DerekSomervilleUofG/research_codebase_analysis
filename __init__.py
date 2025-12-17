from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from repository_save.class_structure.File import File as SuperClass

class File(SuperClass):

    control_populate = LocalControlPopulate()
    
    def __init__(self, name, repository) -> None:
        super().__init__(name)
        self.repository = repository
        self.populate_structure = self.control_populate.get_populate_file()
        self.populate_structure.add_structure(self)
        
from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Repository import Repository as SuperClass

class Repository(SuperClass):
    
    local_control_populate = LocalControlPopulate()

    def __init__(self, name, packages, primary_key=0):
        super().__init__(name, primary_key)
        self.populate_repository = self.local_control_populate.get_populate_repository()
        self.populate_repository.add_structure(self)
        self.packages = packages
        self.start_date = None
    
    def get_start_date(self, start_date):
        if self.start_date is None or start_date < self.start_date:
            self.start_date = start_date
        return self.start_date
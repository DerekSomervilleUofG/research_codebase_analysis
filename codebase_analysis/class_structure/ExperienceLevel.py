from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure
class ExperienceLevel(Structure):
    
    field_code = "code"
    field_score = "score"
    control_populate = LocalControlPopulate()
    
    def __init__(self, data) -> None:
        self.code = data[self.field_code]
        super().__init__(self.code)
        self.score = data[self.field_score]
        self.populate_structure = self.control_populate.get_populate_experience_level()
        self.populate_structure.add_structure(self)
         
    def get_code(self):
        return self.code
    
    def get_score(self):
        return self.score
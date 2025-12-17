from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from class_structure.Structure import Structure

class CommitClass(Structure):

    control_populate = LocalControlPopulate()
    
    def __init__(self, class_structure, amendment_type, commit_id, repository) -> None:
        super().__init__(class_structure.name)
        self.class_structure = class_structure
        self.amendment_type = amendment_type
        self.commit_id = commit_id
        self.repository = repository
        self.populate_structure = self.control_populate.get_populate_commit_class()
        self.populate_structure.add_structure(self)
        
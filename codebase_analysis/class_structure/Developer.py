from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from repository_save.class_structure.Developer import Developer as SuperClass
from utility.ListUtility import ListUtility
class Developer(SuperClass):
    
    local_control_populate = LocalControlPopulate()
    year_increase = 10000000000

    def __init__(self, name, email, login=None, start_date=None, primary_key=0):
        super().__init__(name, email, login, primary_key)
        self.start_date = start_date
        self.populate_developer = self.local_control_populate.get_populate_developer()
        self.populate_developer.add_structure(self)

    def get_end_date(self, no_of_years=1):
        end_date = 0
        if self.start_date is not None:
            end_date = self.start_date + (self.year_increase * no_of_years) 
        return end_date
    
    def find_by_name_and_email(name, email, list_to_search):
        developer = ListUtility.find_in_list_by_name(list_to_search, name)
        if developer is None:
            developer = next(iter(structure for structure in list_to_search if structure.email == email), None)
        return developer
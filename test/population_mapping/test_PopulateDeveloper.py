from unittest import TestCase
from codebase_analysis.class_structure.Developer import Developer
from codebase_analysis.population_mapping.PopulateDeveloper import PopulateDeveloper
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL

class TestPopulateDeveloper(TestCase):
    
    developer = Developer("Derek", "derek.somerville@glasgow.ac.uk", "derek.somerville", 20240819)
    populate_developer = PopulateDeveloper(DBExecuteSQL())
    
    def test_developer_get_name(self):
        self.assertEqual("Derek", self.developer.get_name())
    
    def test_generate_row(self):
        self.assertEqual( ["Derek", "derek.somerville@glasgow.ac.uk", "derek.somerville", "20240819"] ,self.populate_developer.generate_row(self.developer))
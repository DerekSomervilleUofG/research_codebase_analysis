from codebase_analysis.class_structure.Developer import Developer
from unittest import TestCase

class TestDeveloper(TestCase):
    
    developer = Developer("Derek", "derek.somerville@glasgow.ac.uk", "derek.somerville")
    
    def test_get_name(self):
        self.assertEqual("Derek", self.developer.get_name())
from unittest import TestCase
from codebase_analysis.DeterminePackages import DeterminePackages
from repository_save.population_mapping.ControlPopulate import ControlPopulate

class TestDeterminePackages(TestCase):
     
     determine_packages = DeterminePackages(None)

     def test_determine_top_level_with_root(self):
          file_paths = [
                    "root/package1/module1/submodule1/file1.py",
                    "root/package1/module1/submodule2/file2.py",
                    "root/package1/module2/file3.py",
                    "root/package2/module3/submodule4/file4.py",
                    "root/package2/module4/file5.py",
                    "root/package3/file6.py",
                    "root/package2/module3/submodule5/file7.py"
                ]
          self.assertEqual(["root/package1", "root/package2", "root/package3"], self.determine_packages.determine_top_level(file_paths))

     def test_determine_top_level(self):
          file_paths = [
                    "package1/module1/submodule1/file1.py",
                    "package1/module1/submodule2/file2.py",
                    "package1/module2/file3.py",
                    "package2/module3/submodule4/file4.py",
                    "package2/module4/file5.py",
                    "package3/file6.py",
                    "package2/module3/submodule5/file7.py"
                ]
          self.assertEqual(["package1", "package2", "package3"], self.determine_packages.determine_top_level(file_paths))
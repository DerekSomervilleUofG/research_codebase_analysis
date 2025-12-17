from unittest import TestCase
from codebase_analysis.population_mapping.PopulateDeveloperCommit import PopulateDeveloperCommit
from codebase_analysis.class_structure.DeveloperCommit import DeveloperCommit
from codebase_analysis.class_structure.Repository import Repository
from codebase_analysis.class_structure.Developer import Developer
class TestPopulateDeveloperCommit(TestCase):
    
    populate_developer_commit = PopulateDeveloperCommit(None)
    repository_name = "https://stgit.dcs.gla.ac.uk/DerekSomerville/database_batch_save.git"
    repository = Repository(repository_name)
    developer = Developer("derek", "derek.somerville@glasgow.ac.uk", "derek")
    developer_commit = DeveloperCommit("123", "author", "20240819", "", repository, developer)
    
    def test_generate_row(self):
        self.developer_commit.set_repo_count(1, 2, 3)
        self.developer_commit.set_amend_count(4, 5, 6)
        self.assertEqual(["123", "20240819", '0', '0', 1, 2, 3, 4, 5, 6], self.populate_developer_commit.generate_row(self.developer_commit))
from unittest import TestCase
from codebase_analysis.PriorCurrentRepoExperience import PriorCurrentRepoExperience
class TestPriorCurrentRepoExperience(TestCase):
    
    prior_current_repo_experience = PriorCurrentRepoExperience()
    
    def test_determine_package(self):
        files = []
        files.append("/src/main/java/amend/amend.java")
        self.assertEqual("['/src/main/java/amend/']", self.prior_current_repo_experience.determine_package(["/src/main/java/amend/"], files))
    
    def test_determine_package_mutiple(self):
        files = []
        files.append("/src/main/java/amend/amend.java")
        self.assertEqual("['/src/main/java/amend/', '/src/main/java/']", self.prior_current_repo_experience.determine_package(["/src/main/java/amend/", "/src/main/java/"], files))
    
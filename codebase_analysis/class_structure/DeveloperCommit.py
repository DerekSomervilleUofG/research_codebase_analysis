from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from repository_save.class_structure.DeveloperCommit import DeveloperCommit as SuperClass
from repository_save.population_mapping.PopulatePackage import PopulatePackage
from repository_save.population_mapping.PopulateCommitFile import PopulateCommitFile
class DeveloperCommit(SuperClass):
    
    
    store_repo_packages = True
    local_control_populate = LocalControlPopulate()


    def __init__(self, name, author, date, message, repository, developer):
        super().__init__(name, author, date, message, repository, developer)
        self.populate_developer_commit = self.local_control_populate.get_populate_developer_commit()
        self.populate_developer_commit.add_structure(self)
    
    def set_amend_count(self, file_count, class_count, method_count):
        self.file_count = file_count
        self.class_count = class_count
        self.method_count = method_count      
    
    def set_repo_count(self, file_count, class_count, method_count):
        self.repo_file_count = file_count
        self.repo_class_count = class_count
        self.repo_method_count = method_count
    
    def populate_packages(self, packages, prior_knowledge_id):
        for package in packages:
            self.populate_package.insert_package_and_file(package, self.name, self.repository.repository_id, prior_knowledge_id)

    def populate_commit_and_prior_knowledge(self):
        self.populate_packages(self.packages, 0)

    def populate_packages(self, commit_id, packages):
        populate_package = PopulatePackage()

    def populate_commit(self):
        self.populate_packages(self.name, self.packages)
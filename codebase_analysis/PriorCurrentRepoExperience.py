from codebase_analysis.class_structure.PriorAmendCommit import PriorAmendCommit
from codebase_analysis.class_structure.PriorTotalCommit import PriorTotalCommit
from codebase_analysis.class_structure.AmendCommit import AmendCommit
from codebase_analysis.class_structure.FileAtCommit import FileAtCommit
from codebase_analysis.population_mapping.PopulateCommitFile import PopulateCommitFile
from codebase_analysis.population_mapping.PopulateCommitClass import PopulateCommitClass
from codebase_analysis.population_mapping.PopulateCommitMethod import PopulateCommitMethod
from codebase_analysis.class_structure.File import File
from codebase_analysis.class_structure.CommitFile import CommitFile
from codebase_analysis.class_structure.ClassStructure import ClassStructure
from codebase_analysis.class_structure.CommitClass import CommitClass
from codebase_analysis.class_structure.Method import Method
from codebase_analysis.class_structure.CommitMethod import CommitMethod
from utility.ListUtility import ListUtility

class PriorCurrentRepoExperience():
    
    batch_size = 100
    no_of_days = 365
    
    def __init__(self) -> None:
        self.files = []
        
    def delete_files(self):
        for file in self.files:
            file.delete_classes()
        self.files = []

    def set_database(self, control_populate):
        self.populate_commit_file = PopulateCommitFile(control_populate.get_db_execute_sql())
        self.populate_commit_class = PopulateCommitClass(control_populate.get_db_execute_sql())
        self.populate_commit_method = PopulateCommitMethod(control_populate.get_db_execute_sql())
        self.delete_files()
    
    def add_file(self, name, repository):
        file = ListUtility.find_in_list_by_name(self.files, name)
        if file is None:
            file = File(name, repository)
            self.files.append(file)
        return file
    
    def add_class(self, name, file_name, repository):
        file = self.add_file(file_name, repository)
        class_structure = ListUtility.find_in_list_by_name(file.classes, name)
        if class_structure is None:
            class_structure = ClassStructure(name, file, repository)
            file.add_class(class_structure)
        return class_structure
    
    def add_method(self, full_method_name, repository):
        file_name = ""
        class_name = ""
        method_name = full_method_name
        if "&" in full_method_name:
                class_name = full_method_name.split("&")[1]
                file_name = full_method_name.split("&")[0]
                method_name = full_method_name.split("&")[-1]
        class_structure = self.add_class(class_name, file_name, repository)
        method = ListUtility.find_in_list_by_name(class_structure.methods, method_name)
        if method is None:
            method = Method(method_name, class_structure, repository)
            class_structure.add_method(method)
        return method
        
    def get_data_for_entity(self, populate_entity, developer):
        commit_known = {}
        commit_has = {}
        prior_entity = []
        commit_file_cursor = populate_entity.prepare_batch_select(developer.get_primary_key(), developer.get_end_date())
        populate_entity.has_next = True
        commit_id = None
        previous_commit_id = []
        all_count = 0
        known_count = 0
        while populate_entity.has_next:
            commit_entities = populate_entity.next_batch_select(commit_file_cursor, self.batch_size)
            for row in commit_entities:
                if commit_id is None or commit_id != row[1]:
                    if commit_id is not None:
                        if commit_id not in commit_known:
                            commit_known[commit_id] = known_count
                        else:
                            commit_known[commit_id] += known_count
                        previous_commit_id.append(commit_id)
                    commit_id = row[1]
                    known_count = 0
                if row[0] in prior_entity:
                    known_count += 1
                else:
                    prior_entity.append(row[0] )
                if commit_id not in commit_has:
                    commit_has[commit_id] = []
                commit_has[commit_id].append(str(row[2]) + "$" + str(row[3]))
            if commit_id not in commit_known:
                commit_known[commit_id] = known_count
            else:
                previous = commit_known[commit_id]
                commit_known[commit_id] += known_count
        return commit_has, commit_known
    
    def merge_list(self, total_list, list_to_merge):
        for item in list_to_merge:
            if item.split("$")[1] == "ADDED":
                if item.split("$")[0] not in total_list:
                    total_list.append(item.split("$")[0])
            elif item.split("$")[1] == "DELETED":
                if item.split("$")[0] in total_list:
                    total_list.remove(item.split("$")[0])
        return total_list
    
    def determine_package(self, repo_packages, commit_files, packages):
        temp_files = commit_files.copy()
        counter = 0
        package_found = False
        for package in repo_packages:
            package_name = package.split("/")[-1]
            package_found = False
            counter = 0
            while counter < len(temp_files) and not package_found:
                if package_name in temp_files[counter]:
                    package_found = True
                    if package not in packages:
                        packages.append(package)
                counter += 1
        return packages
        
    def create_amend_commit(self, repository, developer, commit_id, total_number_of_files, total_number_of_classes, total_number_of_methods, commit_files, commit_classes, commit_methods, packages):
        if commit_id in commit_classes:
            no_of_classes = len(commit_classes[commit_id])
        else:
            no_of_classes = 0
        if commit_id in commit_methods:
            no_of_methods = len(commit_methods[commit_id])
        else:
            no_of_methods = 0
        packages = self.determine_package(repository.packages, commit_files[commit_id], packages)
        amend_commit = AmendCommit(commit_id, str(packages), total_number_of_files, total_number_of_classes, total_number_of_methods, len(commit_files[commit_id]), no_of_classes , no_of_methods, developer, repository)

    def create_prior_amend_commit(self, repository, developer, commit_id, commit_files, commit_classes, commit_methods):
        if commit_id in commit_classes:
            no_of_classes = commit_classes[commit_id]
        else:
            no_of_classes = 0
        if commit_id in commit_methods:
            no_of_methods = commit_methods[commit_id]
        else:
            no_of_methods = 0
        prior_commit = PriorAmendCommit(commit_id, commit_files[commit_id], no_of_classes , no_of_methods, developer, repository)
    
    def create_file_at_commit(self, commit_id, files, developer, repository):
        for file in files:
            file_at_commit = FileAtCommit(commit_id, file,developer, repository)
            
    def create_commit_method(self, method_name, amendment_type, commit_id, repository):
        method = self.add_method(method_name, repository)
        commit_method = CommitMethod(method, amendment_type, commit_id, repository)
    
    def create_commit_methods(self, methods, commit_id, repository):
        for method in methods:
            amendment_type = ""
            method_name = method
            if "$" in method:
                amendment_type = method.split("$")[1]
                method_name = method.split("$")[0] 
            self.create_commit_method(method_name, amendment_type, commit_id, repository)
                
    
    def create_commit_class(self, class_name, amendment_type, commit_id, file_name, repository):
        class_structure = self.add_class(class_name, file_name, repository)
        commit_class = CommitClass(class_structure, amendment_type, commit_id, repository)
    
    def create_commit_classes(self, classes, commit_id, repository):
        for class_name in classes:
            amendment_type = ""
            file_name = ""
            if "$" in class_name:
                amendment_type = class_name.split("$")[1]
                class_name = class_name.split("$")[0]
            if "&" in class_name:
                file_name = class_name.split("&")[0]
                class_name = class_name.split("&")[-1]
            self.create_commit_class(class_name, amendment_type, commit_id, file_name, repository)
    
    def create_commit_file(self, file_name, commit_id, repository):
        amendment_type = ""
        if "$" in file_name:
            amendment_type = file_name.split("$")[1]
            file_name = file_name.split("$")[0]
        file = self.add_file(file_name, repository)
        commit_file = CommitFile(file, amendment_type, commit_id, repository)
        
    def create_commit_files(self, files, commit_id, repository):
        for file in files:
            self.create_commit_file(file, commit_id, repository)
        
    def run(self, developer, repository):
        delimiter = "$"
        total_files = []
        total_classes = []
        total_methods = []
        packages = []
        commit_files, file_commit_knowledge_known = self.get_data_for_entity(self.populate_commit_file, developer)
        commit_classes, class_commit_knowledge_known = self.get_data_for_entity(self.populate_commit_class, developer)
        commit_methods, method_commit_knowledge_known = self.get_data_for_entity(self.populate_commit_method, developer)
        for commit_id in commit_files.keys():
            prior_total_commit = PriorTotalCommit(commit_id, len(total_files), len(total_classes) , len(total_methods), developer, repository)
            total_files = self.merge_list(total_files, commit_files[commit_id])
            self.create_commit_files(commit_files[commit_id], commit_id, repository)
            if commit_id in commit_classes:
                total_classes = self.merge_list(total_classes, commit_classes[commit_id])
                self.create_commit_classes(commit_classes[commit_id], commit_id, repository)
            if commit_id in commit_methods:
                total_methods = self.merge_list(total_methods, commit_methods[commit_id])
                self.create_commit_methods(commit_methods[commit_id], commit_id, repository)
            self.create_amend_commit(repository, developer, commit_id, len(total_files), len(total_classes), len(total_methods), commit_files, commit_classes, commit_methods, packages)        
            self.create_prior_amend_commit(repository, developer, commit_id, file_commit_knowledge_known, class_commit_knowledge_known, method_commit_knowledge_known)
            
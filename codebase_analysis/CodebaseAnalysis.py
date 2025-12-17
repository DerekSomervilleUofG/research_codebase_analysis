from codebase_analysis.population_mapping.LocalControlPopulate import LocalControlPopulate
from repository_save.population_mapping.ControlPopulate import ControlPopulate
from codebase_analysis.class_structure.Developer import Developer
from codebase_analysis.class_structure.Repository import Repository
from codebase_analysis.class_structure.DeveloperCommit import DeveloperCommit
from codebase_analysis.class_structure.PriorAmendCommit import PriorAmendCommit
from codebase_analysis.population_mapping.PopulateDeveloperCommit import PopulateDeveloperCommit
from codebase_analysis.population_mapping.PopulateDeveloper import PopulateDeveloper
from codebase_analysis.population_mapping.PopulatePriorAmendCommit import PopulatePriorAmendCommit
from codebase_analysis.PriorCurrentRepoExperience import PriorCurrentRepoExperience
from utility.ListUtility import ListUtility
from repository_save.data_source.DatabaseCreate import DatabaseCreate
from codebase_analysis.DeterminePackages import DeterminePackages
from codebase_analysis.class_structure.DeveloperNew import DeveloperNew
from codebase_analysis.class_structure.DeveloperStart import DeveloperStart
from datetime import datetime
from dateutil.relativedelta import relativedelta
class CodebaseAnalysis():
    
    destination_control_populate = LocalControlPopulate()
    
    batch_size = 100
    date_format = "%Y%m%d%H%M%S"   
    
    def __init__(self) -> None:
        self.prior_current_repo_experience = PriorCurrentRepoExperience()
        database_create = DatabaseCreate(self.destination_control_populate.get_db_execute_sql())
        database_create.tables = ["repository", "developer", "developer_commit", "file", "commit_file", "experience_level", "prior_amend_commit", "prior_total_commit", "amend_commit", "file_at_commit", "class", "commit_class", "method", "commit_method", "developer_start", "developer_new"]
        database_create.delete_tables = []
        self.developers = []
        self.destination_control_populate.set_db_file_name("resource/database/codebase.db")
        database_create.setup()
        self.get_destination_developers(self.destination_control_populate.get_populate_developer())
        self.repo_developers = []
        
    def set_database(self, control_populate):
        db_execute_sql = control_populate.get_db_execute_sql()
        self.populate_developer_commit = PopulateDeveloperCommit(db_execute_sql)
        self.populate_prior_amend_commit = PopulatePriorAmendCommit(db_execute_sql)
        self.populate_developer = PopulateDeveloper(db_execute_sql)
        self.populate_repository = control_populate.get_populate_repository()
        self.prior_current_repo_experience.set_database(control_populate)
        self.determine_packages = DeterminePackages(control_populate)
        self.repo_developers = []
        
    def get_destination_developers(self, populate_developer):
        select_cursor = populate_developer.prepare_batch_select()
        while populate_developer.has_next:
            developers = self.get_developers_from_database(select_cursor, self.batch_size, populate_developer)
       
    def get_developers_from_database(self, select_cursor, batch_size, populate_developer):
        developers = []
        sql_data = populate_developer.next_batch_select(select_cursor, batch_size)
        for row in sql_data:
            developer = Developer.find_by_name_and_email(row[1], row[2], self.developers)
            if developer is None:
                developer = Developer(row[1], row[2], row[3], int(row[4]), row[0])
                self.developers.append(developer)
            else:
                developer.start_date = int(row[4])
                developer.primary_key = int(row[0])
            developers.append(developer)
        return developers
    
    def get_repository(self):
        sql_data = self.populate_repository.select_record()
        row = sql_data[0]
        repository = Repository(row[2], self.determine_packages.run(row[0]))
        return repository
    
    def get_developer_commit(self, select_cursor, batch_size, repository, developer, start_date):
        developer_commits = []
        counter = 0
        sql_data = self.populate_developer_commit.next_batch_select(select_cursor, batch_size)
        while counter < len(sql_data):
            row = sql_data[counter]
            developer_commit = DeveloperCommit(row[0], "", str(row[1]), "", repository, developer)
            developer_commit.set_repo_count(row[2], row[3], row[4])
            start_date = datetime.strptime(str(row[1]), self.date_format)
            if developer.name not in self.repo_developers:
                if start_date < repository.get_start_date(start_date) + relativedelta(months=6):
                    developer_start = DeveloperStart(developer, repository)
                else:
                    developer_new = DeveloperNew(developer, repository, len(sql_data))
                self.repo_developers.append(developer.name)
            developer_commits.append(developer_commit)
            self.process_commit(developer_commit)
            counter += 1
        return developer_commits, start_date
    
    def get_prior_commit(self, select_cursor, batch_size, repository, developer, start_date):
        counter = 0
        sql_data = self.populate_prior_amend_commit.next_batch_select(select_cursor, batch_size)
        while counter < len(sql_data):
            row = sql_data[counter]
            prior_commit = PriorAmendCommit(row[0], row[2], row[3], row[4], repository, developer)
            counter += 1
        return start_date
    
            
    def process_commit(self, developer_commit):
        pass
    
    def process_commits(self, developer, repository):
        select_cursor = self.populate_developer_commit.prepare_batch_select(developer.get_primary_key(), developer.get_end_date())
        self.populate_developer_commit.has_next = True
        start_date = None
        while self.populate_developer_commit.has_next:
            developer_commits, start_date = self.get_developer_commit(select_cursor, self.batch_size, repository, developer, start_date)

    def process_prior_commits(self, developer, repository):
        select_cursor = self.populate_prior_amend_commit.prepare_batch_select(developer.get_primary_key())
        self.populate_prior_amend_commit.has_next = True
        start_date = None
        while self.populate_prior_amend_commit.has_next:
            start_date = self.get_prior_commit(select_cursor, self.batch_size, repository, developer, start_date)


    def process_developers(self, developers, repository):
        for developer in developers:
            self.process_commits(developer, repository)
            self.prior_current_repo_experience.run(developer, repository)
            #self.process_prior_commits(developer, repository)
            developer.set_primary_key(0)
            
    def run(self, control_populate):
        self.set_database(control_populate)
        repository = self.get_repository()
        self.populate_developer.has_next = True
        select_cursor = self.populate_developer.prepare_batch_select_with_start_date()
        counter = 0
        while self.populate_developer.has_next:
            developers = self.get_developers_from_database(select_cursor, self.batch_size, self.populate_developer)
            self.process_developers(developers, repository)
            self.destination_control_populate.save_all()
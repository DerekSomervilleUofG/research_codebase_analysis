from codebase_analysis.population_mapping.PopulateRepository import PopulateRepository
from codebase_analysis.population_mapping.PopulateDeveloperCommit import PopulateDeveloperCommit
from codebase_analysis.population_mapping.PopulateDeveloper import PopulateDeveloper
from codebase_analysis.population_mapping.PopulateDeveloperExperience import PopulateDeveloperExperience
from codebase_analysis.population_mapping.PopulateExperienceLevel import PopulateExperienceLevel
from codebase_analysis.population_mapping.PopulatePriorAmendCommit import PopulatePriorAmendCommit
from codebase_analysis.population_mapping.PopulatePriorTotalCommit import PopulatePriorTotalCommit
from codebase_analysis.population_mapping.PopulateAmendCommit import PopulateAmendCommit
from codebase_analysis.population_mapping.PopulateFile import PopulateFile
from codebase_analysis.population_mapping.PopulateCommitFile import PopulateCommitFile
from codebase_analysis.population_mapping.PopulateClass import PopulateClass
from codebase_analysis.population_mapping.PopulateCommitClass import PopulateCommitClass
from codebase_analysis.population_mapping.PopulateMethod import PopulateMethod
from codebase_analysis.population_mapping.PopulateCommitMethod import PopulateCommitMethod
from codebase_analysis.population_mapping.PopulateDeveloperNew import PopulateDeveloperNew
from codebase_analysis.population_mapping.PopulateDeveloperStart import PopulateDeveloperStart
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
class LocalControlPopulate():

    __instance = None

    def __new__(cls, *args, **kwargs):
        if LocalControlPopulate.__instance is None:
            LocalControlPopulate.__instance = super(LocalControlPopulate, cls).__new__(cls, *args, **kwargs)
        return LocalControlPopulate.__instance

    def __init__(self):
        self.db_execute_sql = DBExecuteSQL()
        self.populate_repository = PopulateRepository(self.db_execute_sql)
        self.populate_developer = PopulateDeveloper(self.db_execute_sql)
        self.populate_developer_commit = PopulateDeveloperCommit(self.db_execute_sql)
        self.populate_developer_experience = PopulateDeveloperExperience(self.db_execute_sql)
        self.populate_experience_level = PopulateExperienceLevel(self.db_execute_sql)
        self.populate_prior_amend_commit = PopulatePriorAmendCommit(self.db_execute_sql)
        self.populate_prior_total_commit = PopulatePriorTotalCommit(self.db_execute_sql)
        self.populate_amend_commit = PopulateAmendCommit(self.db_execute_sql)
        self.populate_file = PopulateFile(self.db_execute_sql)
        self.populate_commit_file = PopulateCommitFile(self.db_execute_sql)
        self.populate_class = PopulateClass(self.db_execute_sql)
        self.populate_commit_class = PopulateCommitClass(self.db_execute_sql)
        self.populate_method = PopulateMethod(self.db_execute_sql)
        self.populate_commit_method = PopulateCommitMethod(self.db_execute_sql)
        self.populate_developer_new = PopulateDeveloperNew(self.db_execute_sql)
        self.populate_developer_start = PopulateDeveloperStart(self.db_execute_sql)
        self.database = None
        
    def set_db_file_name(self, db_file_name):
        self.database = db_file_name
        self.db_execute_sql.set_db_file_name(db_file_name)

    def get_db_execute_sql(self):
        return self.db_execute_sql

    def save_all(self):
        self.populate_experience_level.save_rows()
        self.populate_repository.save_rows()
        self.populate_developer.save_rows()
        self.populate_developer_commit.save_rows()
        self.populate_prior_amend_commit.save_rows()
        self.populate_prior_total_commit.save_rows()
        self.populate_amend_commit.save_rows()
        self.populate_file.save_rows()
        self.populate_commit_file.save_rows()
        self.populate_class.save_rows()
        self.populate_commit_class.save_rows()
        self.populate_method.save_rows()
        self.populate_commit_method.save_rows()
        self.populate_developer_new.save_rows()
        self.populate_developer_start.save_rows()
        
    def get_populate_developer(self):
        return self.populate_developer
    
    def get_populate_repository(self):
        return self.populate_repository
    
    def get_populate_developer_commit(self):
        return self.populate_developer_commit
       
    def get_populate_developer_experience(self):
        return self.populate_developer_experience
    
    def get_populate_experience_level(self):
        return self.populate_experience_level
    
    def get_populate_prior_amend_commit(self):
        return self.populate_prior_amend_commit
    
    def get_populate_prior_total_commit(self):
        return self.populate_prior_total_commit
    
    def get_populate_amend_commit(self):
        return self.populate_amend_commit
    
    def get_populate_file(self):
        return self.populate_file
    
    def get_populate_commit_file(self):
        return self.populate_commit_file
    
    def get_populate_class(self):
        return self.populate_class
    
    def get_populate_commit_class(self):
        return self.populate_commit_class
    
    def get_populate_method(self):
        return self.populate_method
    
    def get_populate_commit_method(self):
        return self.populate_commit_method
    
    def get_populate_developer_new(self):
        return self.populate_developer_new
    
    def get_populate_developer_start(self):
        return self.populate_developer_start
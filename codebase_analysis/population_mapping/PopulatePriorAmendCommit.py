from repository_save.population_mapping.PopulateStructureIndividual import PopulateStructureIndividual
from utility.UtilityText import UtilityText

class PopulatePriorAmendCommit(PopulateStructureIndividual):
    
    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "prior_amend_commit"
        self.all_columns = "commit_id, number_of_known_files, number_of_known_classes, number_of_known_methods, developer_id, repository_id"
        self.primary_key = "experience_level_id"
        
    def populate_structure_id(self, structures, structure_id, structure_dict):
        pass
    
    def select_prior_commit(self, developer_id):
        select_statement = "select dc.commit_id, dc.authored_date, count(distinct(cf.file_id)), count(distinct(cc.class_id)), count(distinct(cm.method_id)) "
        select_statement += "from developer_commit dc, commit_file cf "
        select_statement += "left join commit_class cc on "
        select_statement += " cc.commit_id = cf.commit_id "
        select_statement += " left join commit_method cm on "
        select_statement += " cm.commit_id = cc.commit_id "
        select_statement += " inner join prior_file pf on cf.commit_id = pf.commit_id and cf.file_id = pf.file_id"
        select_statement += " inner join prior_class pc on cf.commit_id = pc.commit_id and cc.class_id = pc.class_id"
        select_statement += " inner join prior_method pm on cf.commit_id = pm.commit_id and cm.method_id = pm.method_id"
        select_statement += " where dc.commit_id = cf.commit_id "
        select_statement += " and dc.developer_id = " + str(developer_id)
        select_statement += " group by dc.commit_id "
        return select_statement
    
    def prepare_batch_select(self, developer_id):
        return self.db_execute_sql.prepare_batch_select(self.select_prior_commit(developer_id))

    def generate_row(self, prior_commit):
        return [UtilityText.formate_text(prior_commit.get_name()), prior_commit.no_of_files, prior_commit.no_of_classes, prior_commit.no_of_methods, prior_commit.get_developer_id(), prior_commit.get_repository_id() ]
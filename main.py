from repository_save.Main import Main as RepositoryMain
from repository_save.data_source.DatabaseCreate import DatabaseCreate
from codebase_analysis.CodebaseAnalysis import CodebaseAnalysis
from codebase_analysis.LoadJson import LoadJson
import sys

class Main(RepositoryMain):

    exclusive_lock = False

    def __init__(self) -> None:
        super().__init__()
        self.codebase_analysis = CodebaseAnalysis() 
        #self.load_json = LoadJson()
        #self.load_json.load()
 
        
    def process_database(self, control_populate):
        super().process_database(control_populate)
        self.codebase_analysis.run(control_populate)
    
    def raise_exception(self, ex):
        raise ex
    
    def after_database(self, database):
        pass
    
    def database_setup(self):
        pass
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "../refactor_code_base/src/resource/database/"  
    main = Main()
    main.main(directory)


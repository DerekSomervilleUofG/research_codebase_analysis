from utility.ReadWriteFile import ReadWriteFile
from codebase_analysis.class_structure.ExperienceLevel import ExperienceLevel
import json

class LoadJson():
    
    read_write_file = ReadWriteFile()
    experience_tag = "experience_levels"
    
    def load(self):
        content = self.read_write_file.get_file_as_string("experience.json", "resource/config/")
        data = json.loads(content)
        for experience_data in data[self.experience_tag]:
            experience_level = ExperienceLevel(experience_data)
            print("load", "experience_level", experience_level.get_code(), experience_level.get_score()) 
        
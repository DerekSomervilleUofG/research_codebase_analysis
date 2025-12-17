from codebase_analysis.population_mapping.PopulateFile import PopulateFile

class DeterminePackages():

    batch_size = 500

    def __init__(self, source_control_populate) -> None:
        self.source_control_populate = source_control_populate
        if source_control_populate is not None:
            self.populate_file = PopulateFile(self.source_control_populate.get_db_execute_sql())

    def get_files(self, repository_id):
        select_cursor = self.populate_file.prepare_batch_select(repository_id)
        self.populate_file.has_next = True
        all_files = []
        while self.populate_file.has_next:
            files = self.populate_file.next_batch_select(select_cursor, self.batch_size)
            all_files += files
        return all_files  

    def get_packages(self, files):
        file_packages = []
        for file in files:
            file_split = file[1].split("/")
            if len(file_split) > 1:
                package_split_lowest = file_split[0:-1]
                package_lowest = "/".join(package_split_lowest)
                if package_lowest not in file_packages and "test" not in package_lowest:
                    file_packages.append(package_lowest)
        return file_packages
    
    def get_max_depth(self, files):
        max_depth = 0
        for file in files:
            if max_depth < len(file.split("/")):
                max_depth = len(file.split("/"))
        return max_depth

    def split_files_by_max_depth(self, files, max_depth):
        max_depth_files = []
        less_files = []
        for file in files:
            if max_depth == len(file.split("/")):
                max_depth_files.append(file)
            else:
                less_files.append(file)
        return max_depth_files, less_files

    def determine_top_level(self, files):
        top_level_package = []
        file_packages = self.get_packages(files)
        while len(file_packages) > 2:
            top_level_package = file_packages
            max_depth = self.get_max_depth(file_packages)
            max_depth_files, less_files = self.split_files_by_max_depth(file_packages, max_depth)
            max_depth_files = self.get_packages(max_depth_files)
            file_packages = max_depth_files + less_files
            
        return top_level_package

    def run(self, repository_id):
        files = self.get_files(repository_id)
        return self.determine_top_level(files)
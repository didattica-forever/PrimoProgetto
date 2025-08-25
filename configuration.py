import os


class Configuration:
    HOME_DIRECTORY = os.path.expanduser("~")
    
    WORKING_DIRECTORY = f"{HOME_DIRECTORY}/.passwdgen"
    
    PROFILE = f"{WORKING_DIRECTORY}/passwdgen.profile"
    
    def __init__(self):
        self.check_home_directory()
        self.check_profile()
    
    def check_home_directory(self):
        if not os.path.exists(Configuration.WORKING_DIRECTORY):
            os.makedirs(Configuration.WORKING_DIRECTORY)
            print(f"{Configuration.WORKING_DIRECTORY} created!")
            
    def check_profile(self):
        if not os.path.exists(Configuration.PROFILE):
            self.create_profile()
            self.read_profile()
        else:
            self.read_profile()
            
    def create_profile(self):
        
        
        print(f"{Configuration.PROFILE} created!")
        pass
    
    def read_profile(self):
        pass
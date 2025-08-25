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
        with open(Configuration.PROFILE, "w") as file:
            file.write("###\n")
            file.write("### Passwdgen Profile V 1.0\n")
            file.write("###\n")
            file.write("default_passwd_length 8 # default password length if none specified\n")
            file.write("default_charset ascii_min,ascii_max,num # default password charset\n")
            file.write("charset ascii_min qwertyuiopasdfghjklzxcvbnm\n")
            file.write("charset ascii_max QWERTYUIOPASDFGHJKLZXCVBNM\n")
            file.write("charset num 1234567890\n")
            file.write("charset special $?@#+-_\n")
            file.write("\n\n\n\n\n")
            file.write("### END OF PROFILE\n")
            
        
        print(f"{Configuration.PROFILE} created!")
        pass
    
    def read_profile(self):
        pass
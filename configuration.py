import os


class Configuration(object):
    HOME_DIRECTORY = os.path.expanduser("~")
    
    WORKING_DIRECTORY = f"{HOME_DIRECTORY}/.passwdgen"
    
    PROFILE = f"{WORKING_DIRECTORY}/passwdgen.profile"
    
    PASSWORD_LENGTH = None
    LOWERCASE = None
    UPPERCASE = None
    NUMBERS = None
    SPECIAL = None
    
    #
    # Singleton Pattern for the class
    #
    def __new__(cls, *args, **kwargs):
        # print("__new__")
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configuration, cls).__new__(cls)
        return cls.instance
    
    
    def __init__(self):
        # print("__init__")
        self.instance.check_home_directory()
        self.instance.check_profile()
    
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
            file.write("default_charset charset_min,charset_max,charset_num # default password charset\n")
            file.write("charset_letters qwertyuiopasdfghjklzxcvbnm\n")
            file.write("charset_num 1234567890\n")
            file.write("charset_special $?@#+-_\n")
            file.write("\n\n\n\n\n")
            file.write("### END OF PROFILE\n")
            
        
        print(f"{Configuration.PROFILE} created!")
        pass
    
    def read_profile(self):
        with open(Configuration.PROFILE, "r") as file:
            count = 1
            for line in file:
                line = line.strip()
                if line.startswith('#') or len(line.strip()) == 0:
                    count += 1
                    continue
                
                self.process_line(line)
                count += 1
            
    def process_line(self, line):
        arr = line.split(' ')
        if len(arr) <2:
            return
        parm = arr[0].strip()
        value = arr[1].strip()
        # print(f"parm={parm} is {value}")
        if parm == 'default_passwd_length':
            Configuration.PASSWORD_LENGTH = int(arr[1])        
        if parm == 'charset_letters':
            Configuration.LOWERCASE = arr[1].lower()
            Configuration.UPPERCASE = arr[1].upper()
        if parm == 'charset_num':
            Configuration.NUMBERS = arr[1]
        if parm == 'charset_special':
            Configuration.SPECIAL = arr[1]
    

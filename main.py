from configuration import Configuration
from builder import Builder

configuration_object = Configuration()

def main():
    print("Hello from passwordgenerator!")
    home_dir = Configuration.HOME_DIRECTORY
    print(f"Home directory is {home_dir}")
    
   # configuration_object = Configuration()
    print(f"Run parameters:")
    print(f"\tConfiguration Password Length is {Configuration.PASSWORD_LENGTH}")
    print(f"\tLowercase charset is {Configuration.LOWERCASE}")
    print(f"\tUppercase charset is {Configuration.UPPERCASE}")
    print(f"\tNumbers charset is {Configuration.NUMBERS}")
    print(f"\tSpecial charset is {Configuration.SPECIAL}")

    
    print(Builder().build().generate())
    
    


if __name__ == "__main__":
    main()



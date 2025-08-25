import getopt
import sys
from configuration import Configuration
from builder import Builder

configuration_object = Configuration()

def main():
    # parsing arguments with getopt
    
    argumentList = sys.argv[1:] # Remove 1st argument from the list of command line arguments
    # Options
    options = "hl:"
    # Long options
    long_options = ["help","length=",
                    "min-lower=","min-upper=","min-numbers=","min-specials=",
                    "no-lower", "no-upper", "no-numbers", "no-specials",
                    "with-letters=", "with-lower=", "with-upper=", "with-numbers=", "with-specials="
                    ]
    
    builder = Builder()
    
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)   
        for currentArgument, currentValue in arguments:
            # print(f"***>{currentArgument}={currentValue}")
            if currentArgument in ("-h", "--help"):
                help()
                exit(0)
            if currentArgument in ("--length"):
                builder.with_length(int(currentValue))                
            elif currentArgument in ("--min-lower"):
                builder.with_min_lower(int(currentValue))
            elif currentArgument in ("--min-upper"):
                builder.with_min_upper(int(currentValue))   
            elif currentArgument in ("--min-numbers"):
                builder.with_min_numbers(int(currentValue))
            elif currentArgument in ("--min-specials"):
                builder.with_min_specials(int(currentValue))
            elif currentArgument in ("--no-lower"):
                builder.with_no_lower()                 
            elif currentArgument in ("--no-upper"):
                builder.with_no_upper() 
            elif currentArgument in ("--no-numbers"):
                builder.with_no_numbers()          
            elif currentArgument in ("--no-specials"):
                builder.with_no_specials()
            elif currentArgument in ("--with-letters"):
                builder.with_letters(currentValue)
            elif currentArgument in ("--with-lower"):
                builder.with_lower(currentValue)
            elif currentArgument in ("--with-upper"):
                builder.with_upper(currentValue)
            elif currentArgument in ("--with-numbers"):
                builder.with_numbers(currentValue)                         
            elif currentArgument in ("--with-specials"):
                builder.with_specials(currentValue)                          
    except getopt.error as err:
    # output error, and return with an error code
        print (str(err))
        exit(1)
    # end parsing
    
    
    print(builder.build().generate())
    
    
def help():
    print(f"""
          -h --help - this help
          --length=n - the password length
          --no-lower - don't use lowercase characters
          --no-upper - don't use uppercase characters
          --no-numbers - don't use digits
          --no-specials - don't use special characters
          --min-lower=n - minumum number of lowercase chars the password will contain
          --min-upper=n - minumum number of uppercase chars the password will contain
          --min-numbers=n - minumum number of digits the password will contain
          --min-specials=n - minumum number of special chars the password will contain
          --with-letters=str - set the lowercase and uppercase alphabet (could require escaping \\xxx)
          --with-lower=str - set the lowercase alphabet (could require escaping \\xxx)
          --with-upper=str - set the uppercase alphabet (could require escaping \\xxx)
          --with-numbers=str - set the vailables digits (could require escaping \\xxx)
          --with-specials=str - set the special chars string (could require escaping \\xxx)
    """)
    pass

if __name__ == "__main__":
    main()



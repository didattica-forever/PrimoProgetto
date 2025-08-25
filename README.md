# (PasswordGenerator) 
Tested on linux

Singleton and builder patter rough implementation

Configuration file available at ~/.passwdgen/passwdgen.profile

Usage:
python3 ./main.py [options]

python3 ./main.py --help 
          --help - this help 
          --length=n - the password length 
          --no-lower - don't use lowercase characters 
          --no-upper - don't use uppercase characters 
          --no-numbers - don't use digits 
          --no-specials - don't use special characters 
          --min-lower=n - minumum number of lowercase chars the password will contain 
          --min-upper=n - minumum number of uppercase chars the password will contain 
          --min-numbers=n - minumum number of digits the password will contain 
          --min-specials=n - minumum number of special chars the password will contain 
          --with-letters=str - set the lowercase and uppercase alphabet (could require escaping \xxx) 
          --with-lower=str - set the lowercase alphabet (could require escaping \xxx) 
          --with-upper=str - set the uppercase alphabet (could require escaping \xxx) 
          --with-numbers=str - set the vailables digits (could require escaping \xxx) 
          --with-specials=str - set the special chars string (could require escaping \xxx) 
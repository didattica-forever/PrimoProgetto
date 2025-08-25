import random;
from configuration import Configuration
from random import randrange

#
# builder pattern
#
class Builder:
    def __init__(self):
        self.pwd_length = Configuration.PASSWORD_LENGTH
        self.lower = Configuration.LOWERCASE
        self.upper = Configuration.UPPERCASE
        self.nummbers = Configuration.NUMBERS
        self.specials = Configuration.SPECIAL
        self.min_lower = 0
        self.min_upper = 0
        self.min_numbers = 0
        self.min_specials = 0
        
    def with_no_lower(self):
        self.lower = None
        return self
        
    def with_lower(self, lower):
        self.lower = lower
        return self
        
    def with_min_lower(self, min_lower):
        self.min_lower = min_lower
        return self
        
    def with_no_upper(self):
        self.upper = None
        return self
                    
    def with_upper(self, upper):
        self.upper = upper
        return self
    
    def with_min_upper(self, min_upper):
        self.min_upper = min_upper
        return self
        
    def with_no_numbers(self):
        self.nummbers = None
        return self
        
    def with_numbers(self, numbers):
        self.nummbers = numbers
        return self
            
    def with_min_numbers(self, min_numbers):
        self.min_numbers = min_numbers
        return self
        
    def with_no_pecials(self):
        self.specials = None
        return self
          
    def with_pecials(self, specials):
        self.specials = specials
        return self
    
    def with_min_specials(self, min_specials):
        self.min_specials = min_specials
        return self
    
    def build(self):
        return self.PasswordGenerator(Configuration.PASSWORD_LENGTH, 
                                      Configuration.LOWERCASE,
                                      Configuration.UPPERCASE,
                                      Configuration.NUMBERS,
                                      Configuration.SPECIAL,
                                      self.min_lower,
                                      self.min_upper,
                                      self.min_numbers,
                                      self.min_specials)
    

    
    class PasswordGenerator:
        
        def __init__(self, pwd_length, lower, upper, nummbers, specials, min_lower, min_upper, min_numbers, min_specials):
            self.pwd_length = pwd_length
            self.lower = self.shuffle(lower)
            self.upper = self.shuffle(upper)
            self.numbers = self.shuffle(nummbers)
            self.specials = self.shuffle(specials)
            self.complete = self.join(self.lower, self.upper, self.numbers, self.specials)
            self.min_lower = min_lower
            self.min_upper = min_upper
            self.min_numbers = min_numbers
            self.min_specials = min_specials
            
        def generate(self):
            self.print()
            passwd = ""
            passwd += self.generate_lower(self.min_lower)
            passwd += self.generate_upper(self.min_upper)
            passwd += self.generate_numbers(self.min_numbers)
            passwd += self.generate_specials(self.min_specials)
            passwd += self.generate_complete(self.pwd_length - self.min_lower - self.min_upper - self.min_numbers - self.min_specials)
            return self.shuffle(passwd)[:self.pwd_length]
        
        def generate_lower(self, count):
            if self.lower != None and count > 0:
                str = ""
                for i in range(0, count):
                    str += self.lower[randrange(len(self.lower))]
                return str
            return "" 
               
        def generate_upper(self, count):
            if self.upper != None and count > 0:
                str = ""
                for i in range(0, count):
                    str += self.upper[randrange(len(self.upper))]
                return str
            return ""
               
        def generate_numbers(self, count):
            if self.numbers != None and count > 0:
                str = ""
                for i in range(0, count):
                    str += self.numbers[randrange(len(self.numbers))]
                return str
            return ""
                       
        def generate_specials(self, count):
            if self.specials != None and count > 0:
                str = ""
                for i in range(0, count):
                    str += self.specials[randrange(len(self.specials))]
                return str
            return ""
                       
        def generate_complete(self, count):
            if self.complete != None and count > 0:
                str = ""
                for i in range(0, count):
                    str += self.complete[randrange(len(self.complete))]
                return str
            return ""
        
        
        
        def shuffle(self, str):
            if str == None:
                return None
            l = list(str)
            random.shuffle(l)
            return ''.join(l)
        
        def join(self, lower, upper, numbers, specials):
            str = self.shuffle(f"{lower}{upper}{numbers}{specials}")
            return str
        
        def print(self):
            str = f"lower==>{self.lower}\nupper==>{self.upper}\nnumbers==>{self.numbers}\nspecials==>{self.specials}\ncomplete==>{self.complete}"
            print(str)
            
        
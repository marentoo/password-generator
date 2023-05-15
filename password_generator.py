import secrets

lettersUp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lettersLow = [x.lower() for x in lettersUp]
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = ['~','!','@','#','$','%','*','.',':','+','-','^','&']

print('Welcome to simple password generetor by marento!')
chose_size = int(input('\nPlease enter length of your password: '))
special_signs = (input('\nPlease enter if you want special signs in the password. yes / no: '))

if special_signs == 'yes':
    specials = specials
else:
    specials = []

class PasswordSet:
    def __init__(self, size):
        self.size = size
        
    def create_list(self,lst):
        self.lst  = lst
        return self
    
pass_setting = PasswordSet(chose_size).create_list(lettersUp + lettersLow + numbers + specials)

class Generator:
    def __init__(self, pass_setting):
        self.pass_setting = pass_setting
        self.your_password = self.generate
     
    def generate(self):
        your_password = ""
        for p in range(self.pass_setting.size):
            your_password += secrets.choice(self.pass_setting.lst)
        return your_password

password1 = Generator(pass_setting).generate()
print(f'Your password is: {password1}')
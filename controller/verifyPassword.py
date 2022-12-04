import re
import random
import string

class verifyPassword:
    def validate(password):
        describe = '' ##poor ##moderate ##strong
        contador = 0
        specialChars = False

        ##
        regex = re.compile(r'([!+-=?#%*@&^$_])')
        
        ##
        size = len(password)

        ##Special characters
        if(regex.search(password) != None):
            specialChars = True

        ##Validar rango del string
        upper = any(passw.isupper() for passw in password)
        if (upper == True): contador = contador + 1

        lower = any(passw.islower() for passw in password)
        if (lower == True): contador = contador + 1

        number = any(passw.isdigit() for passw in password)
        if (number == True): contador = contador + 1

        if (specialChars == True): contador = contador + 1
        
        ##isPoor
        if contador < 3 and size < 8:
            describe = 'isPoor'

        ##isModerate
        if contador == 3 and (size >= 8 and size <= 10):
            describe = 'isModerate'

        ##isStrong
        if contador == 4 and size >= 10:
            describe = 'isStrong'
        
        return describe
    
    def getPassword():
        ##Generating
        minusculas = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
        mayusculas = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        number = str(random.randint(0,100))
        specialCharts = ''.join(random.choice(string.punctuation ) for i in range(4))

        ##Get password
        password = minusculas + number + specialCharts + mayusculas
        ##
        return password
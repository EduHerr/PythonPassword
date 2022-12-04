import sys
sys.path.append(r'./')

from controller.fileManage import *
from controller.verifyPassword import *

class Principal:
    def __init__(self):
        self.txtOne = ''
        self.data = {}
        self.main()

    def main(self):
        system = False
        try:
            while system != True:
                ###Menu
                option = int(input("""
                    Hellow world! Chooise an option and write the number of option that you preffer
                    1.-Analyze passwords
                    2.-Get a password
                    3.-Greeting
                """))

                ###Case
                match option:
                    case 1:
                        ##Analizar contrasenias
                        Result = self.checkPasswords()
                        ##Imprimir resultado
                        print("""
                            Numero de contrasenias verificadas: [""", Result['verifiedPasswords'],"""]
                            Nombre del archivo resultado: [""", Result["nameFile"],"""]
                        """)
                    case 2:
                        repit = True
                        while repit != False:
                            userName = input("Write your name\n")

                            ##Validate
                            if len(userName) >= 20:
                                print("You should write only 20 letters for your name, please")
                            else:
                                repit = False
                        ##Get the password
                        cNewPassword = verifyPassword.getPassword()
                        ##Print
                        print("""
                            Dear """, userName, """ your password will: '""",cNewPassword,"""'
                        """)
                        ##
                        answer = int(input("""
                            Wish save the password?
                            1. Yes
                            2. No
                        """))
                        
                        if answer == 1:
                            ##Save the data
                            self.txtOne = fileManage.readFile('Users-Pwds(10).txt')
                            newData = self.formaterList()
                            newData.append({"name": userName, "password": cNewPassword, "describe":''})
    
                            # print(newData)

                            self.data = newData
                            newContent = self.toString()
                            ##write a new text file
                            fileManage.writeFile('Users-Pwds(10).txt', newContent)
                    case 3:
                        print("""
                            Este programa es cortesia de Eduardo Herrera
                        """)
                        exit()
                    case _:
                        print("This option is not valite. Please, write another option")
        except Exception as ex:
            print(ex)
    
    def checkPasswords(self):
        contraseniasVerificadas = 0
        datas = []

        ##Extraer la info del primer archivo de txt
        self.txtOne = fileManage.readFile('Users-Pwds(10).txt')
        _usuarios = self.formaterList()

        ##Iterar lista para validar la password
        for user in _usuarios:
            ##Verify password
            result = verifyPassword.validate(user['password'])
            ##Set result to verifyPassword
            user['describe'] = result
            datas.append(user)
            contraseniasVerificadas = contraseniasVerificadas + 1
        ##
        self.data = datas
        newContent = self.toString()
        ##write a new text file
        fileManage.writeFile('Users-Pwds-Chked.txt', newContent)

        return {"verifiedPasswords": contraseniasVerificadas, "nameFile": 'Users-Pwds-Chked.txt'}

    def formaterList(self): ##Return a list of objects
        _users = []

        for text in self.txtOne:
            ##Obtener el indice de ','
            iComa = text.index(',')
            ##Obtener longitud del string
            leng = len(text)

            ##Extraer [name]
            name = text[0:iComa]
            name = name.strip()
            ##Extraer [password]
            password = text[(iComa+1):leng]
            password = password.strip()

            _users.append({'name': name, 'password': password, 'describe': ''})
        
        return _users
        
    def toString(self):
        cadena = ''
        ###
        for obj in self.data:
            cadena = cadena + obj['name'] + ',' + obj['password'] + ',' + obj['describe'] + '\n'
        ##
        return cadena
####
principal = Principal()
import sys
sys.path.append(r'./')

class fileManage:
    def readFile(nameFile):
        try:
            routeFile = './' + nameFile
            file = open(routeFile)
            readed = file.readlines()
            file.close()
        except Exception as ex:
            print(ex)
        
        return readed
    
    def writeFile(nameFile, content):
        try:
            routeFile = './' + nameFile
            file = open(routeFile, "w")
            file.write(content)
            return
        except Exception as ex:
            print(ex)
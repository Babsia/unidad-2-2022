import csv
import re
from mail import email
class manejador:
    __mailsL=[]
    __cont=0
    def __init__(self):
        self.__mailsL=[]
    def testmail(self):
        archivo = open('mailsarch.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            for i in range(0,len(fila)):
                
                mailtest=email()
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',fila[i].lower()):
                    mailtest.crearCuenta(fila[i])
                    self.__mailsL.append(mailtest)
            
        return
    def retorna (self):
        for i in range(0,len(self.__mailsL)):
            print(self.__mailsL[i].Retornaemail())
    def calculoid(self,idcuenta):
        
        for i in range(0,len(self.__mailsL)):
            
            if(self.__mailsL[i].getid()==idcuenta):
                self.__cont+=1
        return self.__cont



    
         




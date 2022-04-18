import re
class email:
    __idcuenta=""
    __dominio=""
    __tipodom=""
    __passw=""
    def __init__(self,idc="",dom="",tdom="",passw="1234"):
        self.__idcuenta=idc
        self.__dominio=dom
        self.__tipodom=tdom
        self.__passw=passw
        return
    def Retornaemail(self):
        mailr=self.__idcuenta+"@"+self.__dominio+"."+self.__tipodom
        return(mailr)
    def Getdominio(self):
        return(self.__dominio)
    def crearCuenta(self,mail1):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',mail1.lower()):
            mailpartes=re.split(r'[@.]',mail1)
            self.__dominio=mailpartes[1]
            self.__tipodom=mailpartes[2]
            self.__idcuenta=mailpartes[0]
    def getid(self):
        return(self.__idcuenta)
            
	        


            
        
        
    def controlpass(self,passwX):
        while(passwX!=self.__passw):
            passwX=input("contraseña incorrecta ingresela de nuevo")
        self.__passw=input("ingrese su nueva contraseña")
        print(self.__passw)
        
        return
    def muestramail(self):
        print("{}@{}.{}".format(self.__idcuenta,self.__dominio,self.__tipodom))
        return



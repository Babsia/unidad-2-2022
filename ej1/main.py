from mail import email
from manejadormail import manejador
if __name__=='__main__':
    nombre=input("ingrese su nombre: ")
    mail1=input("ingrese su mail: ")
    e=email()
    e.crearCuenta(mail1)
    print("estimado {} te enviaremos tus mensajes a la direccion {}".format(nombre,e.Retornaemail()))
    control=input("desea cambiar su contraseña? ")
    if(control=="si"):
        pass1=input("ingrese su contraseña actual (por defecto 1234): ")
        e.controlpass(pass1)
    test=email()
    test.crearCuenta("informatica.fcefn@gmail.com")
    test2=manejador()
    test2.testmail()
    dominio=input("ingrrese un id ")
    print("la cantidad de mails con ese id es de : {}".format(test2.calculoid(dominio)))
    



    
    
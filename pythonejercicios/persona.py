
# realizare un programa de registro de identidad


print("HOLA BUENOS DIAS, POR FAVOR REGISTRESE")

name = str(input)("tu nombre: ")
lastName = str(input("Tu apellido: "))
age = int(input("Tu edad: "))
mayor = False

if age >= 18:
    mayor = True

if mayor:
    print("Eres mayor de edad")
else:
    print("Tu ere menor ")
    



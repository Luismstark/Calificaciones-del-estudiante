# realizare un programa que calcule las notas de cada materia cursada 
# notas que seran  ingresados por el maestro
# se sumara el total de las notas y se dividira entre el numero de materias
# si la nota final es menor a 50 esta reprobado, si es mayor a 51 y menor a 70 buen estudiante
# si la nota es mayor a 71 y menor a 98 estudiante dedicado, si es igual identico a 99 se gana una veca y 100$

# trabajemos con funciones 


def nota(notas,name): # esta funcion calculara las notas y lo mostrara en la terminal
    suma = sum(notas)
    numMateria = len(notas)
    notaFinal = suma / numMateria
    if notaFinal <=50:
        print('\n\n__________________________\n')#separador_______________
        print(f"{name} HAS REPROBADO!!!!!")
        print(notaFinal)
        mensaje(0)
        print('\n\n__________________________\n')#separador_______________
        inicio()
    elif notaFinal >= 51 and notaFinal <= 69:
        print('\n\n__________________________\n')#separador_______________
        print(f"BUEN ESTUDIANTE {name} ")
        print("TU NOTA FINAL:" + str(notaFinal))
        mensaje(1)
        print('\n\n__________________________\n')#separador_______________
        inicio()

    elif notaFinal > 70 and notaFinal <= 98:
        print('\n\n__________________________\n')#separador_______________
        print(f"ERES UN ESTUDIANTE DEDICADO {name} ")
        print("TU NOTA FINAL:" + str(notaFinal))
        mensaje(2)
        print('\n\n__________________________\n')#separador_______________
        inicio()
    elif notaFinal == 99:
        print('\n\n__________________________\n')#separador_______________
        print(f"FELICIDADES {name} GANASTE UNA BECA Y $1000")
        saldo ='tu saldo: $1000'
        print("TU NOTA FINAL:" + str(notaFinal))
        print(saldo)
        mensaje(3)
        print('\n\n__________________________\n')#separador_______________
        inicio()



def mensaje(num):# mensaje al final de la nota final
    msm = ["Suerte para la proxima","Puedes mejorar","Vas muy bien","Eres increible"]
    print(msm[num])

def ingresarNota():# funcion que permite ingresar nombre del estudiante y las notas
    print('\n\n--------------------------------\n')#separador_______________
    name = str(input("NOMBRE DE ESTUDIANTE: "))
    # notas
    nota1 = int(input("NOTA 1:"))
    nota2 = int(input("NOTA 2:"))
    nota3 = int(input("NOTA 3:"))
    nota4 = int(input("NOTA 4:"))
    totalNotas = [nota1,nota2,nota3,nota4]
    nota(totalNotas,name)
    



def inicio():

    print('\n\n********************************************\n')#separador_______________
    res = int(input("CALIFICA A TUS ESTUDIANTES\n para iniciar introduce: 1"))
    if res == 1:
        ingresarNota()
    else:
        inicio()
   

inicio()



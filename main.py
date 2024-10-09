import os
from datetime import date

print("Hola mundo")

pi=3.14
print(pi)

name= input("Ingrese un texto:")
print(name)

x= int(input("Enter a number: "))
print(type(x))

x=5

print("The number is " + str(x))

def limpieza_pantalla():
    os.system('clear')



limpieza_pantalla()

first_number = int(input('Type the first number: ')) ;\
second_number = int(input('Type the second number: ')) ;\
print("The sum is: ", first_number + second_number)





print(date.today())
print("Fecha del dia de hoy:" , str(date.today()))







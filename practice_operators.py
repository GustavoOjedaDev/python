# Declara tu edad como variable entera
# Declara tu altura como una variable flotante
# Declarar una variable que almacene un número complejo
# Escriba un script que solicite al usuario ingresar la base y la altura del triángulo y calcular el # área de este triángulo (área = 0,5 x bxh).a

age = 23
height = 1.79
number_complex = 1j

base = float(input("Ingrese la base de un triángulo: "))
altura = float(input("Ingrese la altura de un triángulo: "))

area = 0.5 * base * altura

print(area)


## Escriba un script de Python que muestre la siguiente tabla
## 1 1 1 1 1
## 2 1 2 4 8
## 3 1 3 9 27
## 4 1 4 16 64
## 5 1 5 25 125

print ("n n^0 n^1 n^2 n^3")

for n in range (1, 6):
    print(f"{n}  {n**0}   {n**1}   {n**2}   {n**3}")
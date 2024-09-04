import math
# Día 2: 30 días de programación de Python
first_name = 'Jose'
last_name =  'Ojeda'
full_name = 'José Gustavo Ojeda Lozano'
country = 'Perú'
city = 'Piura'
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False


print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
suma = num_one + num_two
resta = num_one - num_two
multiplica = num_one * num_two
dividir = num_one / num_two
resto = num_two % num_one
potencia = pow(num_two, num_one)
print(suma)
print(resta)
print(multiplica)
print(dividir)
print(f"El resto {num_two} y {num_one} es: {resto}")
print(potencia)

# Calcular el área de un círculo
radio = float(input("Ingresa el radio: \n"))
valor_pi = 3.1415

area_of_circle = valor_pi * (radio ** 2)
print(area_of_circle)

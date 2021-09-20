# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:53:10 2021

@author: nefer
"""
# Ejercicio 1
autos = int(input("Numero de autos que entran a la ciudad: "))
amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0
error = 0
for x in range(autos):
    digito = int(input("Digite ultimo numero de la placa: "))
    if(digito == 1 or digito == 2):
        amarilla = amarilla + 1
    elif(digito == 3 or digito == 4):
        rosa = rosa + 1
    elif(digito == 5 or digito == 6):
        roja = roja + 1
    elif(digito == 7 or digito == 8):
        verde = verde + 1
    elif(digito == 9 or digito == 0):
        azul = azul + 1
    else:
        error = error + 1
        print('error solamente digite el ultimo numero de la placa')
print(f'De los {autos} autos que ingresaron a la ciudad corresponden a:')
print(f'calcomanias amarilla: {amarilla}')
print(f'calcomanias rosa: {rosa}')
print(f'calcomanias roja: {roja}')
print(f'calcomanias verde: {verde}')
print(f'calcomanias azul: {azul}')
print(f'Datos erroneos: {error}')

# Ejercicio 2
print('Entre elefante, jirafa y chimpancé')
animal = input("Digite el animal el cual se categorizara por edad: ")
muestra = 0
if(animal == "elefante"):
    muestra = 20
elif(animal == 'jirafa'):
    muestra = 15
elif(animal == 'chimpancé'):
    muestra == 40
else:
    print('Recuerde que debe escoger una opción valida')
if (muestra != 0):
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0
    error = 0
    for x in range(muestra):
        edad = int(input(f'Digite la edad del {x+1} {animal}: '))
        if (edad >= 0 and edad < 2):
            categoria1 = categoria1 + 1
        elif(edad == 2):
            categoria2 = categoria2 + 1
        elif(edad >= 3):
            categoria3 = categoria3 + 1
        else:
            error = error + 1
            print('error digite edades validas')
    total = muestra - error
    porcentaje1 = categoria1 / total * 100
    porcentaje2 = categoria2 / total * 100
    porcentaje3 = categoria3 / total * 100
    print(f'De los {total} datos validos tenemos: ')
    print(f'{porcentaje1} % tiene entre 0 y 1 año')
    print(f'{porcentaje2} % tiene mas de 1 y menos de 3 año')
    print(f'{porcentaje3} % tiene 3 o mas año')
    
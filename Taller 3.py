# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:53:10 2021

@author: nefer
"""

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

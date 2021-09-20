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
        if(animal == 'jirafa'):
            edad = int(input(f'Digite la edad de la {animal} No {x+1} : '))
        else:
            edad = int(input(f'Digite la edad del {animal} No {x+1} : '))
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

# Ejercicio 3
trabajadores = int(input('Digite la cantidad de trabajadores en la empresa: '))
salarios = ''
total = 0
for x in range(trabajadores):
    horas = int(input(f'Digite las horas laboradas por el {x+1} trabajador: '))
    pago = 0
    if(horas > 0 and horas <= 40):
        pago = horas * 20
    elif(horas > 40):
        pago = 800 + ((horas - 40) * 25)
    else:
        print('digite un valor valido')
    total = total + pago
    if(pago != 0):
        salario = f'El salario del {x+1} trabajador es: ${pago:,} \n'
        salarios = salarios + salario
print(f'EL total a pagar es: ${total:,}')
print(salarios)

# Ejercicio 4
alumnos = int(input('Digite la cantidad de alumos: '))
hombre = 0
mujer = 0
edadHombres = 0
edadMujeres = 0
for x in range(alumnos):
    genero = input('Digite el genero del alumno: ')
    if(genero == 'hombre'):
        hombre = hombre + 1
        edad = int(input('Digite la edad del alumno: '))
        edadHombres = edadHombres + edad
    elif(genero == 'mujer'):
        mujer = mujer + 1
        edad = int(input('Digite la edad de la alumna: '))
        edadMujeres = edadMujeres + edad
    else:
        print('Recueda los datos validos son: hombre o mujer')
promedioHombres = edadHombres / hombre
promedioMujeres = edadMujeres / mujer
print(f'El promedio de edad de los hombres es: {promedioHombres}')
print(f'El promedio de edad de las mujeres es: {promedioMujeres}')

# Ejercicio 5
cantidad = int(input('Digite la cantiduad de numeros: '))
for x in range(cantidad):
    if(x == 0):
        menor = int(input('Digite primer numero: '))
    else:
        numero = int(input(f'Digite {x+1} numero: '))
        if(numero < menor):
            menor = numero
print(f'EL numero menor es: {menor}')

# Ejercicio 6
for x in range(5):
    pesoAnterior = float(input('Digite el peso de la ultima reunion: '))
    peso = 0
    for i in range(10):
        pesobascula = float(input(f'Digite el peso {i+1}: '))
        peso = peso + pesobascula
    promedioPeso = peso / 10
    diferenciaPeso = promedioPeso - pesoAnterior
    if(diferenciaPeso > 0):
        print(f'la persona {x+1} subio de peso \n {diferenciaPeso} Kg')
    elif(diferenciaPeso < 0):
        print(f' la persona {x+1} bajo de Peso \n {diferenciaPeso} Kg')
    else:
        print('La persona {x+1} mantuvo el mismo peso ')

# Ejercicio 7
total = 0
agregar = 'si'
while agregar == 'si':
    precio = float(input('Digite el precio del articulo: '))
    cantidad = int(input('Digite la cantidad de articulos: '))
    if(cantidad > 0 and precio > 0):
        precioArticulo = cantidad * precio
        total = total + precioArticulo
    else:
        print('Digite valores validos')
    agregar = input('Desea agregar otro articulo: ')
print(f'EL total a pagar es: ${total:,}')

# Ejercicio 8
clientes = int(input('Digite la cantidad de clientes: '))
precio = float(input('Digite el precio de la entrada: '))
perdida = 0
for x in range(clientes):
    edad = int(input('Digite la edad del cliente: '))
    if(edad > 4 and edad < 15):
        perdida = perdida + (precio * 0.35)
    elif(edad > 14 and edad < 20):
        perdida = perdida + (precio * 0.25)
    elif(edad > 19 and edad < 46):
        perdida = perdida + (precio * 0.1)
    elif(edad > 45 and edad < 66):
        perdida = perdida + (precio * 0.25)
    elif(edad > 65):
        perdida = perdida + (precio * 0.35)
    elif(edad >= 0 and edad < 5):
        print('NO se permite la entrada a niños menores de 5 años')
    else:
        print('Digite datos validos')
print(f'El teatro dejo de percibir ${perdida:,}')

# Ejercicio 9
cadena = ''
total = 0
for x in range(100):
    ventas = int(input(f'Digite las ventas del vendedor {x+1}: '))
    comision = 0
    if(ventas > 0 and ventas <= 20000000):
        comision = ventas * 0.1
    elif(ventas > 20000000 and ventas < 40000000):
        comision = ventas * 0.15
    elif(ventas >= 4000000 and ventas < 80000000):
        comision = ventas * 0.2
    elif(ventas >= 80000000 and ventas < 160000000):
        comision = ventas * 0.25
    elif(ventas >= 16000000):
        comision = ventas * 0.3
    else:
        print('digite un valor valido')
    total = total + comision
    if(comision != 0):
        strventas = f'Las ventas del {x+1} trabajador es: ${ventas:,}'
        strsalario = f' y su comisión es: ${comision:,} \n'
        cadena = cadena + strventas + strsalario
print(f'EL total a pagar es: ${total:,}')
print(cadena)

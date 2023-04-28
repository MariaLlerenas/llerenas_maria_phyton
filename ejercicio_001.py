print("Bienvenido a tu formulario")
nombre = input("¿Cual es tu nombre?: ")
apellido_1 = input("¿Cual es tu primer apellido?: ")
apellido_2 = input("¿Cual es tu segundo apellido?: ")
año = int(input ("¿En que año naciste?: "))
mes = int(input ("¿En que mes naciste? (numero): "))
dia = int(input ("¿En que dia naciste?: "))



print("A. Este es tu nombre completo en mayusculas: ")
nombre_completo = (nombre + " " + apellido_1 + " " + apellido_2)
nombre_completo_upper =nombre_completo.upper()
print(nombre_completo_upper)


print("B. Este es tu nombre completo en minusculas: " )
nombre_completo_lower =nombre_completo.lower()
print(nombre_completo_lower)


edad = 2022 - año 
print(f"D. Esta es tu edad: {edad} ")


contador=0
for i in nombre_completo:
    if i in "aeiouAEIOU":
        contador=contador+1
print('E. Tu nombre completo tiene ', contador, 'vocales')

def contar_letras(cadena):
    letras = 0

    for c in cadena: 
        if c.isalpha():
            letras += 1
        else: 
            pass
    return letras 
resultado = contar_letras(nombre_completo)
print('F. Tu nombre completo tiene', resultado, 'letras')


def es_numerico (cadena):
    try:
        int(cadena)
        return True
    except ValueError: 
        return False
if es_numerico(edad):
    print('G. Tu edad es un valor numerico TRUE')
else:
    print('G. Tu edad NO es un valor numerico FALSE')


import re

def contiene_caracteres(texto):
    patron = re.compile(r'[a-zA-Z]')

    return bool(patron.search(texto))
print('H. Tu nombre completo es un caracter alfanumerico', contiene_caracteres(nombre_completo))


suma_edad = edad + 10
print('I. Tu edad en 10 años sera:', suma_edad)


























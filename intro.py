#python3 nombrearchivo // python3 intro.py
#Booleans
boolean = True #True o False

#Numerales
num = 10
fl = 10.99

#paseInt() el texto lo convertía en entero. .round para redondear
nuevo_float = float(num)
nuevo_entero = int(fl)

print(nuevo_float)
print(nuevo_entero)

print(round(fl))
import random # importamos una libreria llamada random/me permite crear numeros aleatorios
num_aleatorio = random.randint(2,5) #numero aleratorio entre 2 y 5
print(num_aleatorio)
#cadenas o textos o strings
string = "ABCDEFG"
print("Este es el alfabeto",string) # La coma en automatico me va a agregar un espacio 
print("Este es el alfabeto "+string) # El + concatena las cadenas tal cual
print("Este es un numero", 10)
#print("Este es un numero "+10) no se puede concatenar distintos, hayq ue convertirlo:
print("Este es un numero "+str(10))#es como si tuvieramos el 10 entre comillas
print(f"Este es el alfabeto {string}")

#Métodos que nos pueden servir
string2 = "Hola mundo! soy Elena de Troya y hoy es 5 de septiembre"
print(string2.title()) #La primera letra de cada palabra será mayúscula
print(string2.upper()) #Todas en mayúsculas
print(string2.lower()) # Todas en minúsculas
print(string2.count('oy')) #regresa cuántos 'oy' hay en la cadena
string3 = "Elena|Juana|Pablo|Pedro"
print(string3.split('|')) # va a enlistar y dividir la cadena por cada '|' que haya en el string
print(string2.find('Elena'))# en que posicion está la palabra elena. si regresa -1 es que no lo encontró. es case sensitive

#Las tuplas no pueden ser modificadas una vez que se le asigna un valor/ muy parecidas a una lista. pueden tener mas de un tipo de dato

tupla = ("ABC", 10, 10.3, False)
print(tupla[0])
#tupla[1] = 11 // da error porque no se puede cambiar el valor

#LISTAS / ARRAY / ARREGLO
lista_vacia = []
lista_llena = ["Hugo", "Paco", "Luis"] #0-> Hugo; 1-> Paco; 2-> Luis
print(lista_llena[2])
lista_llena[2] = "Donald"
print(lista_llena)
lista_llena.pop() #Elimina el último dato de mi lista
print(lista_llena)
lista_llena.pop(0) #Elimina el dato en la posición indicada
print(lista_llena)
lista_llena.append("Mickey") #Me agrega un dato al final de mi lista
print(lista_llena)

lista_mix = ["Texto1", "Texto2", 1, False, ["Lista1", "Lista2"] ] #Podemos guardar distintos tipos de valores
lista_nombres = ["Elena", "Juana", "Pedro"]
nuevo_lista = lista_llena + lista_nombres
print(nuevo_lista)

#DICCIONARIOS -> Objetos en Javascript

diccionario_vacio = {}
diccionario = {"nombre": "Elena", "edad":30, "soltera": False, "hobbies": ["leer", "comer", "ver tele"]}
diccionario['estatura'] = 1.67
print(diccionario)
edad = diccionario.pop('edad') # eliminamos esa propiedad de diccionario y el valor lo asignamos a la variable
print(diccionario)
print(edad)



lista_alumnas = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos de Pedro MERN?
lista_alumnas[2]["cursos"].pop(2)
from pprint import pprint #Bonitas nuestras impresiones
print(lista_alumnas)


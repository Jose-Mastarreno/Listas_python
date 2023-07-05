lista =[1315486512, "Jose", "Mastarreno", 20, "jmastarreno6512@utm.edu.ec"]   
print (lista)
#Metodo para agregar un elemento al final de la lista
lista.append("Soltero")
print (lista)
#Metodo para agregar varios elementos al final de la lista
lista.extend(["Portoviejo", 2023] )
print(lista)           
#Metodo para insertar un elemento en la posicion indicada
lista.insert(3, "Ponce")
lista.insert(4, "Mastarreno")
print(lista)
#Funcion para eliminar elemento de la lista
lista.remove(1315486512)
print(lista)
#Metodo para copiar la lista
print("Lista Copiada")
lista.copy()
print(lista)
#Metodo para contar elementos repetidos
repetidos=lista.count("Mastarreno")
print("Elementos repetidos")
print(repetidos)
#Metodo para eliminar todos los elementos de la lista
lista.clear()
print("Elementos Borrados" ,lista)


#Nueva lista
numeros=[7,22,5,14,0,56,33]
print("Nueva Lista")
print(numeros)
numeros.sort()
print("Numeros Ordenados Ascendentes")
print(numeros)
numeros.reverse()
print("Numeros Ordenados Descendentes")
print(numeros)
#Eliminar elementos
del numeros[3]
print(numeros)
#Funcion para extraer un elemento de la lista
print("Extraer sin parametro")
numeros.pop()
print(numeros)
print("Extraer con parametro")
numeros.pop(3)
print(numeros)

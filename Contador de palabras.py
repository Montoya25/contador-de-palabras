#Se le pide al usuario ingresar una oración para contar las palabras
oracion = input("Ingresa la oración: ")

#Split() separa la oración por palabras y las divide
palabras = oracion.split()

#Len() cuenta las palabras que se dividieron
num_pal = len(palabras)

#Se ingresa el texto del output con el espacio para agregar el número de palabras
msj_fin = "La oración tiene {num_pal} palabras."

#Se imprime el texto de salida
print(msj_fin.format(num_pal=num_pal))
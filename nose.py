import os

def renombrar_logs(directorio, prefijo):
    contador = 1
    for archivo in os.listdir(directorio):
        if archivo.endswith(".log"):
            nuevo_nombre = f"{prefijo}_{contador}.log"
            os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))
            contador += 1

# Solicitar la ruta del directorio y el prefijo
directorio = input("Ingrese la ruta del directorio: ")
prefijo = input("Ingrese el prefijo para los nuevos nombres: ")

# Llamar a la función para renombrar los archivos
renombrar_logs(directorio, prefijo)
print("Archivos renombrados.")

# main.py
# Archivo principal del grupo
# Cada integrante deberá agregar su función en un archivo independiente
from funciones import *
from funciones.restar_medina import restar_medina

if __name__ == "__main__":
    print("Ejecución de pruebas de las funciones del grupo")
    
    # Pruebas de restar_medina
    print("10 - 4 =", restar_medina(10, 4))   
    print("5 - 10 =", restar_medina(5, 10))

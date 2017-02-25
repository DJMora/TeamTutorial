"""
Ejemplo de el uso de modulos en Python
"""
from entities import Equipo

def main():
    equipo = Equipo() #Se instancia un objeto de tipo Equipo
    equipo.showInfo() #Llama al metodo showInfo definido en la clase Equipo

if __name__ == "__main__":
    main()

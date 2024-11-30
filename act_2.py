print()
print("Edgar Gael Garcia Camacho 1182 3w:Examen")
print()
class Persona:
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")

    def es_mayor_de_edad(self):
        
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")


def main():
    #Solicitar al usuario los datos de la persona
    nombre = input("Introduce el nombre de la persona: ")
    edad = int(input("Introduce la edad de la persona: "))
    
    #Crear un objeto Persona
    persona1 = Persona(nombre, edad)
    
    #Mostrar los datos y verificar si es mayor de edad
    persona1.mostrar_datos()
    persona1.es_mayor_de_edad()


if __name__ == "__main__":
    main()

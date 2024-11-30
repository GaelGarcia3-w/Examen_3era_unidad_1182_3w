print()
print("Edgar Gael Garcia Camacho 1182 3w:Examen")
class Alumno:
    def __init__(self, nombre, nota):
        #Inicializa los atributos de la clase
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        #Imprime los datos del alumno
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        #Determina si el alumno ha aprobado o no
        if self.nota >= 5:
            print(f" {self.nombre} Has aprobado.")
        else:
            print(f"{self.nombre}, no has aprobado. Necesitas mejorar.")

#Función principal para probar la clase
def main():
    #Crear un objeto Alumno
    nombre = input("Introduce el nombre del alumno: ")
    nota = float(input("Introduce la nota del alumno: "))
    
    alumno1 = Alumno(nombre, nota)
    
    #Mostrar los datos y el resultado
    alumno1.imprimir_datos()
    alumno1.resultado()


if __name__ == "__main__":
    main()

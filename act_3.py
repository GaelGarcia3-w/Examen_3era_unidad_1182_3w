print()
print("Edgar Gael Garcia Camacho 1182 3w:Examen")
print()
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        #Inicializa los atributos de los lados del triángulo
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con el valor mayor es: {mayor}")

    def tipo_triangulo(self):
        #Determina el tipo de triángulo según los lados
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")


def main():
    print("Introduzca las longitudes de los tres lados del triángulo:")
    
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    
    #Crear un objeto Triangulo con los tres lados
    triangulo = Triangulo(lado1, lado2, lado3)
    
    
    triangulo.lado_mayor()
    triangulo.tipo_triangulo()

if __name__ == "__main__":
    main()

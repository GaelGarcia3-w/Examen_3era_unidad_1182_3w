print()
print("Edgar Gael Garcia Camacho 1182 3w:Examen")
print()
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self): return self.num1 + self.num2
    def resta(self): return self.num1 - self.num2
    def multiplicacion(self): return self.num1 * self.num2
    def division(self): return "Error" if self.num2 == 0 else self.num1 / self.num2

#Te pide dos numeros para realizar las operaciones.
num1, num2 = int(input("Introduce el primer número: ")), int(input("Introduce el segundo número: "))

#Genera los resultado
calc = Calculadora(num1, num2)
print(f"Suma: {calc.suma()}, Resta: {calc.resta()}, Multiplicación: {calc.multiplicacion()}, División: {calc.division()}")

# Examen_3era_unidad_1182_3w
Edgar Gael Garcia Camacho 3-W
 # Programa 1.

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

![image](https://github.com/user-attachments/assets/f82bb0e7-0b07-4fed-b1d6-00fbfc823f84) ![image](https://github.com/user-attachments/assets/e138828b-8e79-47e6-b449-5c7fadebb96c)

# Programa 2.

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

![image](https://github.com/user-attachments/assets/3103bad9-8085-4733-bed9-39882e4e9abf) ![image](https://github.com/user-attachments/assets/963065b7-9393-480f-a9c2-f5b47214dab6)

# Programa 3.

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

![image](https://github.com/user-attachments/assets/a44c8a5b-b5f7-4af2-a525-b47c9f370bea) ![image](https://github.com/user-attachments/assets/b0f5f7a5-a7ec-469a-bf08-3c252e3cde90)
![image](https://github.com/user-attachments/assets/4b0dd137-6f9b-445c-ae88-e6f7e4512442)

# Programa 4.

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

![image](https://github.com/user-attachments/assets/e9485825-d31d-4733-943f-25c52689f6a6) ![image](https://github.com/user-attachments/assets/8141225c-42bd-4d4a-b775-d8990f4cb0b4)

# Programa 5.

print()

print("Edgar Gael Garcia Camacho 1182 3w:Examen")

print()

class Agenda:

   def __init__(self):
   
   self.contactos = []

   def añadir_contacto(self):
  
   self.contactos.append({'nombre': input("Nombre: "), 'telefono': input("Teléfono: "), 'email': input("Email: ")})

   def listar_contactos(self):
  
   if self.contactos: 
  
   for c in self.contactos: print(c)
   
   else: print("No hay contactos.")

   def buscar_contacto(self):
  
   nombre = input("Buscar: ")
   
   for c in self.contactos:
   
   if c['nombre'].lower() == nombre.lower(): print(c); return
   
   print("No encontrado.")

   def editar_contacto(self):
  
   nombre = input("Editar: ")
   
   for c in self.contactos:
   
   if c['nombre'].lower() == nombre.lower():
   
   c['telefono'], c['email'] = input("Nuevo teléfono: "), input("Nuevo email: ")
   
   print("Contacto actualizado.")
   
   return
   
   print("No encontrado.")

def menu():
   
   agenda = Agenda()
   
  while (op := input("\n1. Añadir  2. Listar  3. Buscar  4. Editar  5. Salir: ")) != '5':
  
   if op == '1': agenda.añadir_contacto()
   
   elif op == '2': agenda.listar_contactos()
   
   elif op == '3': agenda.buscar_contacto()
  
   elif op == '4': agenda.editar_contacto()
   
   else: print("Opción no válida.")


if __name__ == "__main__":

  menu()

![image](https://github.com/user-attachments/assets/985f0dc9-28aa-46c3-9dd6-c7030f74d45e) ![image](https://github.com/user-attachments/assets/989ff8dd-f432-4192-a3c8-0b5f8c72d9de)



    


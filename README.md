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



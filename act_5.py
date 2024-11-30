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



    

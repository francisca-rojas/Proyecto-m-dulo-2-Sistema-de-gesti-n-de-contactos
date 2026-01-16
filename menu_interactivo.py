# Importa clases del módulo sistema_gestion_contactos
from sistema_gestion_contactos import Contacto, AgendaContactos

# ==========================================
# Funciones de Interfaz (Menú y Captura)
# ==========================================

def solicitar_dato_valido(prompt, atributo_nombre):
    """
    Solicita un dato al usuario y lo valida usando la clase Contacto.

    Parámetros:
    - prompt (str): Mensaje mostrado al usuario.
    - atributo_nombre (str): Tipo de dato a validar 
    ('nombre', 'telefono', 'correo', 'direccion').

    Retorna:
    - str: Valor ingresado válido.
    """   
    #Bucle para asegurar que el usuario ingrese datos que la clase acepte
    while True:
        valor = input(prompt).strip()
        try:
            # Valida usando un contacto temporal
            if atributo_nombre == "nombre": Contacto(valor, "123456789", "a@a.com", "Calle Falsa")
            elif atributo_nombre == "telefono": Contacto("Juan Perez", valor, "a@a.com", "Calle Falsa")
            elif atributo_nombre == "correo": Contacto("Juan Perez", "123456789", valor, "Calle Falsa")
            elif atributo_nombre == "direccion": Contacto("Juan Perez", "123456789", "a@a.com", valor)
            return valor
        except ValueError as e:
            print(f"❌ {e}")

def ejecutar_sistema():
    """
    Ejecuta el menú interactivo del sistema de gestión de contactos.

    Permite al usuario registrar, editar, eliminar, buscar y listar
    contactos mediante un menú por consola.

    Retorna:
    - None
    """
    agenda = AgendaContactos() # Instancia de clase AgendaContactos

    while True:
        print("\n" + "="*45)
        print("📒 SISTEMA DE GESTIÓN DE CONTACTOS (V2.0)")
        print("="*45)
        print("1. Registrar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Buscar por NOMBRE")
        print("5. Buscar por TELÉFONO")
        print("6. Listar todos")
        print("7. Salir")
        
        opc = input("\nSeleccione una opción: ").strip()
        
        # Registra contacto, validando datos y crea un objeto de clase Contacto
        if opc == "1":
            nom = solicitar_dato_valido("Nombre y Apellido (Ejemplo: Juan Perez): ", "nombre")
            tel = solicitar_dato_valido("Teléfono (9 dígitos | Ejemplo: 123456789): ", "telefono")
            cor = solicitar_dato_valido("Correo (Ejemplo: ejemplo@mail.com): ", "correo")
            dir = solicitar_dato_valido("Dirección (Ejemplo: Calle 78): ", "direccion")
            
            nuevo = Contacto(nom, tel, cor, dir)
            exito, msj = agenda.registrar_contacto(nuevo)
            print(msj)

        # Editar objeto de clase Contacto, accediendo mediante su telefono (llave)
        elif opc == "2":
            tel_actual = input("Teléfono del contacto a editar: ").strip()
            contacto = agenda.obtener_por_telefono(tel_actual)
            
            if contacto:
                print(f"\nEditando a: {contacto.nombre}")
                print("(Deje en blanco para mantener el dato actual)")
                try:
                    # 1. Intentar cambiar teléfono
                    nuevo_tel = input(f"Nuevo teléfono [{contacto.telefono}]: ").strip()
                    if nuevo_tel:
                        exito, msj = agenda.actualizar_telefono_agenda(tel_actual, nuevo_tel)
                        print(msj)
                        if not exito: continue # Si falla el cambio de ID, cancelamos edición
                    
                    # 2. Otros datos (nombre, correo, direccion)
                    nuevo_nom = input(f"Nuevo nombre [{contacto.nombre}]: ").strip()
                    if nuevo_nom: contacto.nombre = nuevo_nom
                    
                    nuevo_cor = input(f"Nuevo correo [{contacto.correo}]: ").strip()
                    if nuevo_cor: contacto.correo = nuevo_cor
                    
                    nuevo_dir = input(f"Nueva dirección [{contacto.direccion}]: ").strip()
                    if nuevo_dir: contacto.direccion = nuevo_dir
                    
                    print("✅ Actualización de datos completada.")
                except ValueError as e:
                    print(f"❌ Error en la edición: {e}")
            else:
                print("❌ No se encontró ningún contacto con ese teléfono.")

        # Elimina objeto de clase Contacto, accediendo mediante su telefono (llave)
        elif opc == "3":
            tel = input("Teléfono del contacto a eliminar: ")
            if agenda.eliminar(tel): print("🗑️ Contacto eliminado.")
            else: print("❌ No existe.")

        # Busca un contacto por nombre
        elif opc == "4":
            busqueda = input("Nombre a buscar: ").strip()
            resultados = agenda.buscar_nombre(busqueda)
            if resultados:
                for r in resultados: print(r)
            else: print("❌ Sin coincidencias.")

        # Busca contacto accediendo mediante su telefono
        elif opc == "5":
            tel = input("Teléfono a buscar: ").strip()
            contacto = agenda.obtener_por_telefono(tel)
            if contacto:
                print(f"\nDetalles del contacto:\n{contacto}")
            else: print("❌ No encontrado.")

        # Lista los objetos Contacto en agenda
        elif opc == "6":
            contactos = agenda.listar()
            if not contactos: print("📭 Agenda vacía.")
            else:
                print(f"\n--- LISTADO ({len(contactos)} contactos) ---")
                for c in contactos: print(c)
        
        # Sale del menú interactivo, rompiendo el bucle
        elif opc == "7":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida.")

# Llama a la función para que sea ejecutada
if __name__ == "__main__":
    ejecutar_sistema()
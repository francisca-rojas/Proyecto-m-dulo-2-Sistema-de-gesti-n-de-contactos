# Importa match para validar expresiones 
from re import match

# ==========================================
# Clase Contacto: Validación y Encapsulación
# ==========================================
class Contacto:
    """
    Representa un contacto individual.

    Se encarga de almacenar y validar los datos personales
    (nombre, teléfono, correo y dirección) aplicando encapsulación
    y validaciones mediante métodos getters y setters, y el uso de @property.
    """
    
    def __init__(self, nombre, telefono, correo, direccion):
        """
        Inicializa un contacto validando todos sus datos.

        Parámetros:
        - nombre (str): Nombre y apellido del contacto.
        - telefono (str): Teléfono de 9 dígitos.
        - correo (str): Correo electrónico válido.
        - direccion (str): Dirección del contacto.

        Retorna:
        - None
        """  
         
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion


    @property
    def nombre(self): return self.__nombre
    
    @nombre.setter             # Setters para validar nombre
    def nombre(self, valor):
        if not match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+", valor):
            raise ValueError("Nombre inválido. Debe incluir al menos un Nombre y un Apellido (Juan Pérez).")
        self.__nombre = valor.strip().upper()


    @property
    def telefono(self): return self.__telefono
    
    @telefono.setter            # Setters para validar telefono
    def telefono(self, valor):
        if not match(r"^\d{9}$", valor):
            raise ValueError("El teléfono debe tener exactamente 9 dígitos numéricos.")
        self.__telefono = valor


    @property
    def correo(self): return self.__correo

    @correo.setter              # Setters para validar correo
    def correo(self, valor):
        if not match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', valor.lower()):
            raise ValueError("Correo electrónico no válido (ejemplo@dominio.com).")
        self.__correo = valor.strip().lower()


    @property
    def direccion(self): return self.__direccion
    
    @direccion.setter           # Setters para validar dirección
    def direccion(self, valor):
        if len(valor.strip()) < 4:
            raise ValueError("La dirección es demasiado corta (mínimo 4 caracteres).")
        self.__direccion = valor.strip()


    def __str__(self):          #Mostrar información de objeto contacto
        return f"👤 {self.nombre} | 📞 {self.telefono} | 📧 {self.correo} | 🏠 {self.direccion}"


# ==========================================
# Clase AgendaContactos: Lógica de Almacenamiento
# ==========================================
class AgendaContactos:
    """
    Gestiona los contactos.

    Utiliza un diccionario donde la clave (llave) es el teléfono
    y el valor es un objeto de clase Contacto.
    """
    
    def __init__(self):
        """
        Inicializa una agenda vacía.

        Retorna:
        - None
        """
        self.__contactos = {} # Diccionario {telefono: Objeto Contacto}

    def registrar_contacto(self, contacto):
        """
        Registra un nuevo contacto en la agenda.

        Parámetros:
        - contacto (Contacto): Objeto contacto a registrar.

        Retorna:
        - tuple (bool, str):
            True si se registra correctamente, False si el teléfono ya existe.
            Mensaje descriptivo del resultado.
        """     
        if contacto.telefono in self.__contactos:
            return False, "❌ Error: Ese teléfono ya está registrado."
        self.__contactos[contacto.telefono] = contacto
        return True, "✅ Contacto guardado correctamente."

    def actualizar_telefono_agenda(self, tel_viejo, tel_nuevo):
        """
        Actualiza el teléfono de un contacto y reindexa el diccionario.
        Permite manejar el cambio de llave en el diccionario de forma segura.

        Parámetros:
        - tel_viejo (str): Teléfono actual del contacto.
        - tel_nuevo (str): Nuevo teléfono a asignar.

        Retorna:
        - tuple (bool, str):
            True si la actualización es exitosa.
            False si el nuevo teléfono ya existe.

        Retorna:
        - ValueError si el nuevo teléfono no cumple el formato.
        """
        if tel_nuevo == tel_viejo:
            return True, ""     # No hay cambios que hacer
        if tel_nuevo in self.__contactos:
            return False, "❌ El nuevo teléfono ya pertenece a otro contacto."
        
        # Proceso de re-indexación
        contacto = self.__contactos.pop(tel_viejo) #Elimina y guarda tel_viejo

        try:
            contacto.telefono = tel_nuevo # Esto valida el formato con el setter
            self.__contactos[tel_nuevo] = contacto
            return True, "✅ Teléfono actualizado en el sistema."
        except ValueError as e:
            # Si el nuevo formato es inválido, devolvemos el contacto a su sitio original
            self.__contactos[tel_viejo] = contacto
            raise e

    def eliminar(self, telefono):
        """
        Elimina contacto por parámetro teléfono.

        Parámetros:
        - telefono (str): Teléfono del contacto a eliminar.

        Retorna:
        - bool: True si se eliminó, False si no existía.
        """
        return self.__contactos.pop(telefono, None) is not None

    def buscar_nombre(self, texto):
        """
        Busca contactos por su cuyo nombre.
        Sirve para búsqueda parcial.

        Parámetros:
        - texto (str): Texto a buscar dentro del nombre.

        Retorna:
        - list[Contacto]: Lista de contactos coincidentes.
        """
        return [c for c in self.__contactos.values() if texto.upper() in c.nombre]

    def obtener_por_telefono(self, telefono):
        """
        Obtiene un contacto por su teléfono.

        Parámetros:
        - telefono (str): Teléfono del contacto.

        Retorna:
        - Contacto | None: El contacto encontrado o None si no existe.
        """
        return self.__contactos.get(telefono)

    def listar(self):
        """
        Devuelve todos los contactos registrados.

        Retorna:
        - list[Contacto]: Lista completa de contactos.
        """
        return list(self.__contactos.values())
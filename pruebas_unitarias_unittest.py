# Importa unittest para prueba unitarias
import unittest

# Importa clases Contacto, AgendaContactos desde istema_gestion_contactos
from sistema_gestion_contactos import Contacto, AgendaContactos

# Clase de pruebas, hereda de clase unittest.TestCase
class TestSistemaContactos(unittest.TestCase):
    """
    Conjunto de pruebas unitarias para el sistema de gestión de contactos.

    Verifica el correcto funcionamiento del registro, búsqueda,
    edición, eliminación y validaciones.
    """
    def setUp(self):
        """
        Prepara el entorno antes de cada prueba.
        Crea una agenda limpia y un contacto base reutilizable.

        Retorna:
        - None
        """
        self.agenda = AgendaContactos() # Crea una agenda vacía y un contacto válido
        self.contacto_base = Contacto("Juan Perez", "987654321", "juan@mail.com", "Calle 123")

    # --- Pruebas de Registro ---
    def test_registro_exitoso(self):
        """
        Verifica que un contacto válido se registre correctamente.

        Retorna:
        - None
        """
        exito, msj = self.agenda.registrar_contacto(self.contacto_base)
        self.assertTrue(exito)    # Comprueba registro exitoso
        self.assertEqual(len(self.agenda.listar()), 1)   # Comprueba que hay 1 contacto

    def test_registro_duplicado(self):
        """
        Verifica que no se permitan contactos con teléfonos duplicados.

        Retorna:
        - None
        """
        self.agenda.registrar_contacto(self.contacto_base)
        # Intenta registrar otro contacto con el mismo teléfono
        duplicado = Contacto("Maria Lopez", "987654321", "maria@mail.com", "Avenida 456")
        exito, msj = self.agenda.registrar_contacto(duplicado)
        self.assertFalse(exito)
        self.assertIn("ya está registrado", msj) # Mensaje de error correcto

    # --- Pruebas de Búsqueda ---
    def test_busqueda_por_nombre(self):
        """
        Verifica la búsqueda parcial de contactos por nombre.

        Retorna:
        - None
        """
        self.agenda.registrar_contacto(self.contacto_base) 
        self.agenda.registrar_contacto(Contacto("Juan Alberto", "900000001", "albert@mail.com", "Calle B"))
        
        resultados = self.agenda.buscar_nombre("Juan")
        self.assertEqual(len(resultados), 2)   # Verifica que hay 2 resultados
        self.assertEqual(resultados[0].nombre, "JUAN PEREZ")

    def test_busqueda_por_telefono(self):
        """
        Verifica la búsqueda por telefono, que el contacto existe
        y es el correcto.

        Retorna:
        - None
        """
        self.agenda.registrar_contacto(self.contacto_base)
        encontrado = self.agenda.obtener_por_telefono("987654321")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "JUAN PEREZ")

    # --- Pruebas de Edición ---
    def test_edicion_datos_basicos(self):
        """
        Verifica el cambio y guardado del correo.

        Retorna:
        - None
        """
        self.agenda.registrar_contacto(self.contacto_base)
        # Cambiamos el correo directamente (usando el setter)
        self.contacto_base.correo = "nuevo@mail.com"
        self.assertEqual(self.agenda.obtener_por_telefono("987654321").correo, "nuevo@mail.com")

    def test_cambio_telefono_exitoso(self):
        """
        Verifica el cambio y guardado del telefono.

        Retorna:
        - None
        """
        self.agenda.registrar_contacto(self.contacto_base)
        exito, msj = self.agenda.actualizar_telefono_agenda("987654321", "999888777")
        
        self.assertTrue(exito)
        self.assertIsNone(self.agenda.obtener_por_telefono("987654321")) # El viejo no existe
        self.assertIsNotNone(self.agenda.obtener_por_telefono("999888777")) # El nuevo sí

    # --- Pruebas de Validación (Errores esperados) ---
    def test_validacion_nombre_incorrecto(self):
        """
        Verifica que se lance un ValueError ante un nombre inválido.

        Retorna:
        - None
        """
        # Debe lanzar ValueError si el nombre no tiene apellido o tiene números
        with self.assertRaises(ValueError):
            Contacto("Juan123", "987654321", "juan@mail.com", "Calle 123")

    def test_validacion_correo_incorrecto(self):
        """
        Verifica que se lance un ValueError ante un correo inválido.

        Retorna:
        - None
        """
        with self.assertRaises(ValueError):
            Contacto("Juan Perez", "987654321", "correo-invalido", "Calle 123")

if __name__ == '__main__':
    unittest.main()
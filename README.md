# Sistema de Gestión de Contactos

## Descripción

Sistema de gestión de contactos desarrollado en **Python**, basado en **Programación Orientada a Objetos (POO)** y acompañado de **pruebas unitarias**.

El sistema permite **registrar, editar, eliminar y buscar contactos** desde la consola.
Incluye validaciones para los datos ingresados (nombre, teléfono, correo y dirección) y evita el registro de contactos duplicados.

---

## Organización del proyecto

El proyecto está compuesto por los siguientes archivos principales:

* **`sistema_gestion_contactos.py`**
  Contiene las clases principales del sistema:

  * `Contacto`: representa un contacto individual y valida sus datos.
  * `AgendaContactos`: gestiona el almacenamiento y las operaciones sobre los contactos.

* **`menu_interactivo.py`**
  Contiene el menú interactivo que permite al usuario utilizar el sistema desde la consola.

* **`test_sistema_contactos.py`**
  Contiene las pruebas unitarias que verifican el correcto funcionamiento del sistema.

---

## Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos (POO)
* `unittest` (pruebas unitarias)

---

## Cómo ejecutar el programa

### 1 Requisitos

* Tener **Python 3** instalado en el sistema.

### 2 Entrar a la carpeta del proyecto

```bash
cd sistema-gestion-contactos
```
### 3 Ejecutar el menú interactivo

```bash
python3 menu_interactivo.py
```

---

## Ejemplo de uso

Al iniciar el programa, se muestra el siguiente menú:

```
📒 SISTEMA DE GESTIÓN DE CONTACTOS
1. Registrar contacto
2. Editar contacto
3. Eliminar contacto
4. Buscar por nombre
5. Buscar por teléfono
6. Listar contactos
7. Salir
```

### Ejemplo de registro de un contacto

```
Nombre: Juan Perez
Teléfono: 987654321
Correo: juan@mail.com
Dirección: Calle 123
```

---

## Ejecutar pruebas unitarias

Para verificar el correcto funcionamiento del sistema, ejecuta:

```bash
python3 test_sistema_contactos.py
```

Si todo está correcto, se mostrará un resultado similar a:

```
........
----------------------------------------------------------------------
Ran 8 tests in 0.012s

OK
```

---

## Autora

**Francisca Rojas González**

from empleado import Empleado
import json

class GestorCine:

    def __init__(self):
        self.empleados = []
        self.cargar_empleados()

    def login(self,usuario,contrasena):
        for empleado in self.empleados:
            if empleado.usuario == usuario and empleado.contrasena == contrasena:
                return empleado
        return None

    def añadir_empleado(self,empleado):
        for existente in self.empleados:
            if existente.usuario == empleado.usuario:
                raise ValueError("Ese nombre de usuario ya existe")
            if existente.dni == empleado.dni:
                raise ValueError("Ese DNI ya está registrado")
        self.empleados.append(empleado)
        self.guardar_empleados()

    def modificar_empleado(self, dni, nuevo_usuario,nueva_contrasena):
        for empleado in self.empleados:
            if empleado.dni == dni:
                for existente in self.empleados:
                    if (existente != empleado and existente.usuario == nuevo_usuario):
                        raise ValueError("Ese nombre de usuario ya existe")
                empleado.usuario = nuevo_usuario
                empleado.contraseña = nueva_contrasena
                self.guardar_empleados()
                return True
        return False

    def eliminar_empleado(self, dni):
        for empleado in self.empleados:
            if empleado.dni == dni:
                self.empleados.remove(empleado)
                self.guardar_empleados()
                return True
        return False
    
    def guardar_empleados(self):
        lista_empleados = []
        for empleado in self.empleados:
            datos = {
                "nombre": empleado.nombre,
                "dni": empleado.dni,
                "usuario": empleado.usuario,
                "contrasena": empleado.contrasena,
                "tipo_usuario": empleado.tipo_usuario
            }
            lista_empleados.append(datos)
        with open("empleados.json", "w", encoding="utf-8") as archivo:
            json.dump(lista_empleados, archivo, indent=4, ensure_ascii=False) #escribe informacion sobre un archivo JSON, indent --> espacios, ascii-->guardar carácteres (ñ,´...)

    def cargar_empleados(self):
        try:
            with open("empleados.json", "r", encoding="utf-8") as archivo:
                lista_empleados = json.load(archivo)
                for datos in lista_empleados:
                    empleado = Empleado(
                        datos["nombre"],
                        datos["dni"],
                        datos["usuario"],
                        datos["contrasena"],
                        datos["tipo_usuario"]
                    )
                    self.empleados.append(empleado)
        except FileNotFoundError:
            self.empleados = []
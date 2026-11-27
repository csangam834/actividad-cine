class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} | DNI: {self.dni}"
    
class Cliente(Persona):

    def __init__(self, nombre, dni, importe_total_acumulado=0):
        super().__init__(nombre, dni)
        self.importe_total_acumulado = importe_total_acumulado

    def actualizar_importe(self, precio):
        self.importe_total_acumulado += precio

    def mostrar_datos(self):
        return (
            f"{super().mostrar_datos()} | "
            f"Importe acumulado: {self.importe_total_acumulado:.2f} €"
        )

class Empleado(Persona):
    def __init__(self, nombre, dni, usuario, contrasena, tipo_usuario):

        super().__init__(nombre, dni) #llamar a la clase de la que hereda otra clase.
        if tipo_usuario not in ["Administrador","Empleado"]:#solo puede registrarse como admin o empleado
            raise ValueError("Tipo de usuario no válido")
        
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario

    def mostrar_datos(self):
        return (
            f"{super().mostrar_datos()} | "
            f"Usuario: {self.usuario} | "
            f"Tipo: {self.tipo_usuario}"
        )
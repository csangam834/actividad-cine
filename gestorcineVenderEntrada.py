from datetime import datetime


# =====================================================================
# CLASES DE APOYO TEMPORALES (sustituir por imports)
# =====================================================================
"""
class Pelicula:
    def __init__(self, titulo: str, duracion: int, genero: str = "", clasificacion: str = "", descripcion: str = ""):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.clasificacion = clasificacion
        self.descripcion = descripcion


class Sala:
    def __init__(self, nombre: str, capacidad: int):
        self.nombre = nombre
        self.capacidad = capacidad


class Butaca:
    def __init__(self, sala: Sala, fila: str, numero: int):
        self.sala = sala
        self.fila = fila
        self.numero = numero

    def __eq__(self, otro):
        if not isinstance(otro, Butaca):
            return False
        return (
            self.sala == otro.sala
            and self.fila.upper() == otro.fila.upper()
            and self.numero == otro.numero
        )

    def __str__(self):
        return f"{self.fila.upper()}{self.numero}"


class Sesion:
    def __init__(self, sesion_id: str, pelicula: Pelicula, sala: Sala, fecha_hora: str, precio_base: float):
        self.id = sesion_id
        self.pelicula = pelicula
        self.sala = sala
        self.fecha_hora = fecha_hora
        self.precio_base = float(precio_base)


class Persona:
    def __init__(self, nombre: str, dni: str):
        self.nombre = nombre
        self.dni = dni.upper()


class Cliente(Persona):
    def __init__(self, nombre: str, dni: str, importe_total_acumulado: float = 0.0):
        super().__init__(nombre, dni)
        self.importe_total_acumulado = float(importe_total_acumulado)
        self.historial_entradas = []

    def acumular_compra(self, importe: float, entrada=None):
        self.importe_total_acumulado = round(self.importe_total_acumulado + float(importe), 2)
        if entrada is not None:
            self.historial_entradas.append(entrada)


class Entrada:
    def __init__(self, sesion: Sesion, butaca: Butaca, cliente: Cliente, precio_final: float):
        self.sesion = sesion
        self.butaca = butaca
        self.cliente = cliente
        self.precio_final = float(precio_final)
        self.fecha_compra = datetime.now().isoformat(timespec="seconds")

    def __str__(self):
        return (
            f"Entrada | Película: {self.sesion.pelicula.titulo} | "
            f"Sesión: {self.sesion.fecha_hora} | Butaca: {self.butaca} | "
            f"Cliente: {self.cliente.nombre} ({self.cliente.dni}) | "
            f"Precio Final: {self.precio_final:.2f} €"
        )
"""

# =====================================================================
# GESTOR CINE - MÓDULO DE VENTA Y ACTUALIZACIÓN 
# =====================================================================
class GestorCine:
    def __init__(self, sesiones=None, clientes=None, entradas=None):
        # Pueden pasarse colecciones compartidas con los grupos 5 y 6
        self.sesiones = sesiones if sesiones is not None else {}      # dict[sesion_id, Sesion]
        self.clientes = clientes if clientes is not None else {}      # dict[dni, Cliente]
        self.entradas = entradas if entradas is not None else []      # list[Entrada]

    def _calcular_precio_final(self, sesion: Sesion, cliente: Cliente) -> float:
        """
        Calcula el precio final de la entrada.
        Ajustable según las reglas que defina el equipo (descuentos, recargos, etc.).
        """
        return round(float(sesion.precio_base), 2)

    def vender_entrada(self, sesion_id: str, butaca: Butaca, cliente_data):
        """
        Realiza la venta de una entrada:
        1. Valida que la sesión exista.
        2. Verifica que la butaca pertenezca a la sala de la sesión y esté libre.
        3. Registra o recupera el cliente por DNI.
        4. Calcula el precio final y crea la Entrada.
        5. Actualiza el importe_total_acumulado del cliente y guarda la entrada.
        """
        if sesion_id not in self.sesiones:
            raise ValueError(f"No existe una sesión con ID '{sesion_id}'.")

        sesion = self.sesiones[sesion_id]

        if not isinstance(butaca, Butaca):
            raise TypeError("La butaca debe ser una instancia de Butaca.")

        if butaca.sala != sesion.sala:
            raise ValueError(
                f"La butaca {butaca} no pertenece a la sala '{sesion.sala.nombre}' de la sesión."
            )

        if self._butaca_ocupada(sesion_id, butaca):
            raise ValueError(f"La butaca {butaca} ya está ocupada en la sesión '{sesion_id}'.")

        cliente = self._obtener_o_crear_cliente(cliente_data)
        precio_final = self._calcular_precio_final(sesion, cliente)

        entrada = Entrada(
            sesion=sesion,
            butaca=butaca,
            cliente=cliente,
            precio_final=precio_final,
        )

        # Actualización del cliente y registro de la venta
        cliente.acumular_compra(precio_final, entrada=entrada)
        self.entradas.append(entrada)

        return entrada

"""

if __name__ == "__main__":
    peli = Pelicula("Interstellar", 169, "Ciencia Ficción", "PG-13")
    sala1 = Sala("Sala 1", 100)
    sesion1 = Sesion("S1", peli, sala1, "2026-11-25 19:30", 8.50)

    gestor = GestorCine(sesiones={"S1": sesion1})

    b1 = Butaca(sala1, "A", 1)
    b2 = Butaca(sala1, "A", 2)

    # Primera compra: cliente nuevo
    e1 = gestor.vender_entrada("S1", b1, {"nombre": "Laura Gómez", "dni": "12345678A"})
    print("Venta 1:", e1)
    print("Acumulado Laura:", gestor.clientes["12345678A"].importe_total_acumulado)

    # Segunda compra: mismo cliente (se reutiliza y suma al acumulado)
    e2 = gestor.vender_entrada("S1", b2, {"nombre": "Laura Gómez", "dni": "12345678a"})
    print("Venta 2:", e2)
    print("Acumulado Laura tras 2ª entrada:", gestor.clientes["12345678A"].importe_total_acumulado)

    # Intento de vender butaca ya ocupada
    try:
        gestor.vender_entrada("S1", b1, {"nombre": "Carlos Ruiz", "dni": "87654321B"})
    except ValueError as err:
        print("Error esperado al repetir butaca:", err)
        
"""
class Pelicula:
    def __init__(self, titulo, genero, duracion, clasificacion, descripcion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.descripcion = descripcion

class Sala:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

class Sesion:
    def __init__(self, pelicula, sala, fecha, hora, precio_base):
        self.pelicula = pelicula
        self.sala = sala
        self.fecha = fecha
        self.hora = hora
        self.precio_base = precio_base

class GestorCine:
    def __init__(self):
        self.peliculas = []
        self.salas = []
        self.sesiones = []

    def anadir_pelicula(self, pel):
        if pel not in self.peliculas:
            self.peliculas.append(pel)
            print("La película ha sido añadida correctamente")
        else:
            print("La pelicula ya estaba añadida")

    def modificar_pelicula(self, pel, titulo, duracion, descripcion):
        if pel in self.peliculas:
            pel.titulo = titulo
            pel.duracion = duracion
            pel.descripcion = descripcion
            print("Película modificada correctamente")
        else:
            print("La película no existe")

    def eliminar_pelicula(self,pel):
        if pel in self.peliculas:
            self.peliculas.remove(pel)
            print("Película borrada correctamente")
        else:
            print("La película no existe")

    def anadir_sesion(self,ses):
        if ses not in self.sesiones:
            self.sesiones.append(ses)
            print("La sesion ha sido añadida correctamente")
        else:
            print("La sesion ya estaba añadida")

    def modificar_sesion(self,ses,pelicula,sala,fecha,hora,precio_base):
        if ses in self.sesiones:
            ses.pelicula = pelicula
            ses.sala = sala
            ses.fecha = fecha
            ses.hora = hora
            ses.precio_base = precio_base
            print("Sesion modificada correctamente")
        else:
            print("La sesion no existe")

    def eliminar_sesion(self,ses):
        if ses in self.sesiones:
            self.sesiones.remove(ses)
            print("Sesion borrada correctamente")
        else:
            print("La película no existe")

    def gestionar_peliculas(self):
        salir=False;
        while not salir:
            print("\n--- GESTIÓN DE PELÍCULAS ---")
            print("1. Añadir película")
            print("2. Modificar película")
            print("3. Eliminar película")
            print("0. Volver")

            opcion = input("Introduce una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                genero = input("Género: ")
                duracion = int(input("Duración: "))
                clasificacion = input("Clasificación: ")
                descripcion = input("Descripción: ")

                pel = Pelicula(titulo, genero, duracion, clasificacion, descripcion)
                self.anadir_pelicula(pel)
            elif opcion == "2" or opcion == "3":
                if len(self.peliculas) == 0:
                    print("No hay películas disponibles")
                else:
                    for i in range(len(self.peliculas)):
                        print(f"{i+1}. {self.peliculas[i].titulo}")
                    indice = int(input("Selecciona una película: ")) - 1
                    if 0 <= indice < len(self.peliculas):
                        pel = self.peliculas[indice]
                        if opcion == "2":
                            titulo = input("Nuevo título: ")
                            duracion = int(input("Nueva duración: "))
                            descripcion = input("Nueva descripción: ")
                            self.modificar_pelicula(pel, titulo, duracion, descripcion)
                        else:
                            self.eliminar_pelicula(pel)
                    else:
                        print("Película no válida")
            elif opcion == "0":
                salir=True
            else:
                print("Opción incorrecta")
                
    
    def consultar_cartelera(self):
        print("\n========== CARTELERA ==========")

        for i, sesion in enumerate(self.sesiones):
            print("\nSesion:", i + 1)
            print("Pelicula:", sesion.pelicula.titulo)
            print("Sala:", sesion.sala.nombre)
            print("Fecha:", sesion.fecha)
            print("Hora:", sesion.hora)
            print("Precio:", sesion.precio_base, "€")

    def consultar_disponibilidad(self, sesion_id):
        if sesion_id < 1 or sesion_id > len(self.sesiones):
            print("Sesion no encontrada")
            return

        sesion = self.sesiones[sesion_id - 1]

        print("\n======= DISPONIBILIDAD =======")
        print("Pelicula:", sesion.pelicula.titulo)
        print("Sala:", sesion.sala.nombre)

        for butaca in sesion.sala.butacas:
            ocupada = False

            for entrada in self.entradas:
                if entrada.sesion == sesion and entrada.butaca == butaca:
                    ocupada = True

            if ocupada:
                estado = "OCUPADA"
            else:
                estado = "LIBRE"

            print("Fila:", butaca.fila,
                  "Butaca:", butaca.numero,
                  "-", estado)


def gestionar_sesiones(self):
    salir = False

    while not salir:
        print("\n--- GESTIÓN DE SESIONES ---")
        print("1. Añadir sesión")
        print("2. Modificar sesión")
        print("3. Eliminar sesión")
        print("0. Volver")

        opcion = input("Introduce una opción: ")

        if opcion == "1" or opcion == "2":
            valido = True

            if len(self.peliculas) == 0 or len(self.salas) == 0:
                print("No hay películas o salas disponibles")
                valido = False

            # Seleccionar la sesión que se quiere modificar
            if valido and opcion == "2":
                if len(self.sesiones) == 0:
                    print("No hay sesiones disponibles")
                    valido = False
                else:
                    for i in range(len(self.sesiones)):
                        ses = self.sesiones[i]
                        print(f"{i+1}. {ses.pelicula.titulo} - {ses.fecha} - {ses.hora}")

                    indice = int(input("Selecciona una sesión: ")) - 1

                    if 0 <= indice < len(self.sesiones):
                        ses = self.sesiones[indice]
                    else:
                        print("Sesión no válida")
                        valido = False

            # Seleccionar película
            if valido:
                for i in range(len(self.peliculas)):
                    print(f"{i+1}. {self.peliculas[i].titulo}")

                indicePel = int(input("Selecciona una película: ")) - 1

                if 0 <= indicePel < len(self.peliculas):
                    pel = self.peliculas[indicePel]
                else:
                    print("Película no válida")
                    valido = False

            # Seleccionar sala
            if valido:
                for i in range(len(self.salas)):
                    print(f"{i+1}. {self.salas[i].nombre}")

                indiceSala = int(input("Selecciona una sala: ")) - 1

                if 0 <= indiceSala < len(self.salas):
                    sala = self.salas[indiceSala]
                else:
                    print("Sala no válida")
                    valido = False

            # Solicitar los datos de la sesión
            if valido:
                fecha = input("Introduce la fecha: ")
                hora = input("Introduce la hora: ")
                precio_base = float(input("Introduce el precio base: "))

                if opcion == "1":
                    ses = Sesion(pel, sala, fecha, hora, precio_base)
                    self.anadir_sesion(ses)
                else:
                    self.modificar_sesion(ses, pel, sala, fecha, hora, precio_base)

        elif opcion == "3":
            if len(self.sesiones) == 0:
                print("No hay sesiones disponibles")
            else:
                for i in range(len(self.sesiones)):
                    ses = self.sesiones[i]
                    print(f"{i+1}. {ses.pelicula.titulo} - {ses.fecha} - {ses.hora}")

                indice = int(input("Selecciona una sesión: ")) - 1

                if 0 <= indice < len(self.sesiones):
                    self.eliminar_sesion(self.sesiones[indice])
                else:
                    print("Sesión no válida")

        elif opcion == "0":
            salir = True

        else:
            print("Opción incorrecta")
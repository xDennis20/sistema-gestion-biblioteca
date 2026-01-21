from typing import List

from Libro import Libro
from Usuario import Usuario
from Prestamo import Prestamo

class Biblioteca:
    TOTAL_LIBRO = 0
    TOTAL_USUARIOS = 0

    def __init__(self,nombre: str):
        self.nombre = nombre
        self.usuarios = {}
        self.libros = {}
        self.prestamos_activos: List[Prestamo] = []

    def agregar_libro(self,libro: Libro) -> None:
        if libro.isbn in self.libros:
            libro_existente = self.libros[libro.isbn]
            if libro_existente.tipo == Libro.TIPO_FISICO:
                libro_existente.stock += libro.stock
        else:
            self.libros[libro.isbn] = libro
            Biblioteca.TOTAL_LIBRO += 1

    def agregar_usuario(self,usuario: Usuario) -> None:
        if usuario.dni in self.usuarios:
            raise ValueError("Error: Este usuario ya esta registrado")
        self.usuarios[usuario.dni] = usuario
        Biblioteca.TOTAL_USUARIOS += 1

    def prestar_libro(self,usuario: Usuario,libro: Libro):
        if not usuario.puede_pedir_mas:
            raise ValueError("Error: Usuario alcanzo limite de adquirir libros")
        if not libro.disponible:
            raise ValueError("Error: No hay stock del lbiro")

        crear_prestamo = Prestamo.crear_prestamo_hoy(usuario,libro)
        self.prestamos_activos.append(crear_prestamo)

        usuario.agregar_libro_usuario(libro)

        if libro.tipo == Libro.TIPO_FISICO:
            libro.stock -= 1

        print(f"Prestamo exitoso: {libro.titulo} a {usuario.nombre}")

    def devolver_libro(self,usuario: Usuario, libro: Libro):
        for prestamo in self.prestamos_activos:
            if prestamo.usuario == usuario and prestamo.libro == libro:
                if prestamo.multa > 0:
                    usuario.multa = prestamo.multa
                    print(f"El usuario tiene una multa de ${usuario.multa}")
                libro.stock += 1
                usuario.devolver_libro(libro)
                self.prestamos_activos.remove(prestamo)
                return
        raise "Error: Este usuario no tiene prestado ese libro"

    def __str__(self):
        return (f"--- Biblioteca '{self.nombre}' ---"
                f"Tiene {Biblioteca.TOTAL_LIBRO} Libros"
                f"Y usuarios registrados {self.usuarios} en su biblioteca"
                f"Prestamos activos: {len(self.prestamos_activos)}")
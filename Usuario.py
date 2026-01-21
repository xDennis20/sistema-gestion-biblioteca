from Libro import Libro

class Usuario:
    TIPO_REGULAR = "regular"
    TIPO_VIP = "vip"
    TIPO_LIMITES = {
        TIPO_REGULAR: 3,
        TIPO_VIP: 10
    }
    
    def __init__(self,nombre: str, dni: str, correo: str):
        self.nombre = nombre
        self.dni = dni
        self.correo = correo
        self.tipo = Usuario.TIPO_REGULAR
        self.libros_prestados : list[Libro] = []
        self.multa = None

    @classmethod
    def usuario_regular(cls,nombre: str, dni: str, correo: str) -> Usuario:
        usuario = cls(nombre,dni,correo)
        usuario.tipo = cls.TIPO_REGULAR
        return usuario

    @classmethod
    def usuario_vip(cls,nombre: str, dni: str, correo: str) -> Usuario:
        usuario = cls(nombre,dni,correo)
        usuario.tipo = cls.TIPO_VIP
        return usuario

    def agregar_libro_usuario(self,libro: Libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self,libro: Libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El usuario {self.nombre} no tiene el libro {libro.titulo}")

    @property
    def puede_pedir_mas(self):
        return len(self.libros_prestados) < Usuario.TIPO_LIMITES.get(self.tipo)

    def __eq__(self, other):
        if not isinstance(other,Usuario):
            return NotImplemented
        return self.dni == other.dni

    def __str__(self):
        return f"Usuario {self.nombre}, DNI: {self.dni}, Correo: {self.correo}, Tipo: {self.tipo}"
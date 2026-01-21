from Usuario import Usuario
from Libro import Libro
from datetime import date, datetime, timedelta

class Prestamo:
    PLAZO_PRESTADO = 14

    def __init__(self,usuario: Usuario,fecha_prestamo: date,libro: Libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=Prestamo.PLAZO_PRESTADO)

    @classmethod
    def crear_str_date(cls,usuario: Usuario,fecha_prestamo: str, libro: Libro,):
        fecha_transformada = datetime.strptime(fecha_prestamo,"%d-%m-%Y").date()
        return cls(usuario,fecha_transformada,libro)

    @classmethod
    def crear_prestamo_hoy(cls,usuario: Usuario, libro: Libro):
        return cls(usuario,datetime.now().date(),libro)

    @property
    def retraso_dias(self):
        fecha_actual = datetime.now().date()
        dias_retraso = fecha_actual - self.fecha_vencimiento
        return max(0,dias_retraso.days)

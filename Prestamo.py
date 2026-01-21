from Usuario import Usuario
from Libro import Libro
from datetime import date, datetime, timedelta

class Prestamo:
    PLAZO_PRESTADO = 14
    COSTO_MULTA_DIARA = 0.50

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
    def retraso_dias(self) -> int:
        fecha_actual = datetime.now().date()
        dias_retraso = fecha_actual - self.fecha_vencimiento
        return max(0,dias_retraso.days)

    @property
    def multa(self) -> float:
        if self.usuario.tipo == Usuario.TIPO_VIP:
            return 0.0

        if self.retraso_dias <= 0:
            return 0.0

        return Prestamo.COSTO_MULTA_DIARA * self.retraso_dias

    def __str__(self):
        return (f"--- Pretamo ---"
                f"Usuario: {self.usuario.nombre}"
                f"Libro: {self.libro.titulo}"
                f"Fecha_vencimiento: {self.fecha_vencimiento}")
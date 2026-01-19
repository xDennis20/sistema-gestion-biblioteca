class Libro:
    TIPO_DIGITAL = "digital"
    TIPO_FISICO = "fisico"
    TIPOS_VALIDOS = (TIPO_DIGITAL,TIPO_FISICO)

    def __init__(self, titulo: str, autor: str, isbn: str, years: str):
        if self.validar_str_vacios(titulo) or self.validar_str_vacios(autor) or self.validar_str_vacios(isbn) or self.validar_str_vacios(years):
            raise ValueError("Error: Valor vacio")
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.years = years
        self.tipo = Libro.TIPO_DIGITAL
        self.stock = None

    @staticmethod
    def validar_str_vacios(valor: str) -> bool:
        valor = valor.strip(" ")
        if not valor:
            return True
        return False

    @staticmethod
    def validar_tipo_libro(tipo: str):
        return tipo.lower() in Libro.TIPOS_VALIDOS

    @classmethod
    def libro_digital(cls,titulo: str, autor: str, isbn: str, years:str) -> Libro:
        libro = cls(titulo,autor,isbn,years)
        libro.tipo = cls.TIPO_DIGITAL
        return libro

    @classmethod
    def libro_fisico(cls,titulo:str,autor: str, isbn: str, years: str, stock: int) -> Libro:
        if stock <= 0:
            raise ValueError("Error: El stock debe ser mayor a 0")
        libro = cls(titulo,autor,isbn,years)
        libro.tipo = cls.TIPO_FISICO
        libro.stock = stock
        return libro

    def __eq__(self, other):
        if not isinstance(other,Libro):
            raise NotImplemented
        return self.isbn == other.isbn

    def __lt__(self, other):
        if not isinstance(other, Libro):
            raise NotImplemented
        return self.titulo < other.titulo

    def __str__(self) -> str:
        if self.tipo == Libro.TIPO_DIGITAL:
            return f"Libro: {self.titulo}, Autor: {self.autor} ISBN: {self.isbn}, Año: {self.years} Tipo: {self.tipo}"
        return f"Libro: {self.titulo}, Autor: {self.autor} ISBN: {self.isbn}, Año: {self.years} Tipo: {self.tipo}, Stock: {self.stock}"

    def __repr__(self):
        return f"{type(self).__name__}(titulo='{self.titulo}', autor='{self.autor}, isbn='{self.isbn}, año='{self.years}', tipo='{self.tipo}', stock={self.stock}"
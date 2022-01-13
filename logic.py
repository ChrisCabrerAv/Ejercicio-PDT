class Carrera():
    nombre:str = ""
    lenguaje: int = 0
    matematicas:int = 0 
    ciencias:int = 0
    historia:int = 0
    
    def __init__(self, nombre:str, lenguaje:int, matematicas:int, ciencias:int, historia:int) -> None:
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.matematicas = matematicas
        self.ciencias = ciencias
        self.historia = historia

    def get_nombre(self) -> str:
        return self.nombre

    def get_matematicas(self) -> str:
        return str(self.matematicas)

    def get_lenguaje(self) -> str:
        return str(self.lenguaje)

    def get_ciencias(self) -> str:
        return str(self.ciencias)

    def get_historia(self) -> str:
        return str(self.historia)

    def get_puntaje_lenguaje (self, puntaje) -> str:
        resultado = puntaje * self.lenguaje / 100
        return str(resultado)

    def __repr__(self) -> str:
        return "Carrera: {0}\nPonderaciones: Lenguaje = {1}, Matemáticas = {2}, Ciencias = {3}, Historia = {4}".format(self.nombre, self.lenguaje,self.matematicas,self.ciencias,self.historia)
        
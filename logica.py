class Carrera():
    nombre:str = ""
    nem:int = 25
    ranking:int = 25
    lenguaje: int = 0
    matematicas:int = 0 
    ciencias:int = 0
    historia:int = 0
    puntaje_ultimo = 0
    
    def __init__(self, nombre:str, lenguaje:int, matematicas:int, ciencias:int, historia:int, puntaje_ultimo:int) -> None:
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.matematicas = matematicas
        self.ciencias = ciencias
        self.historia = historia
        self.puntaje_ultimo = puntaje_ultimo

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

    def get_puntaje_ultimo(self) -> str:
        return str(self.puntaje_ultimo)

    def get_puntaje_lenguaje (self, puntaje) -> str:
        resultado = puntaje * self.lenguaje // 100
        return str(resultado)

    def get_puntaje_matematica (self, puntaje) -> str:
        resultado = puntaje * self.matematicas // 100
        return str(resultado)

    def get_puntaje_historia (self, puntaje) -> str:
        resultado = puntaje * self.historia // 100
        return str(resultado)

    def get_puntaje_ciencias (self, puntaje) -> str:
        resultado = puntaje * self.ciencias // 100
        return str(resultado)

    def _calcular(self,nem,ranking,p_len,p_mat,p_cie,p_his):
        puntaje = (nem*self.nem // 100) + (ranking*self.ranking // 100) + (p_len*self.lenguaje // 100) + (p_mat*self.matematicas //100) + (p_cie*self.ciencias//100)+(p_his*self.historia//100)
        return puntaje
    
    def calcular(self,nem,ranking,p_len,p_mat,p_cie,p_his):
        return str(self._calcular(nem,ranking,p_len,p_mat,p_cie,p_his))

    def __repr__(self) -> str:
        return "Carrera: {0}\nPonderaciones: Lenguaje = {1}, Matemáticas = {2}, Ciencias = {3}, Historia = {4}".format(self.nombre, self.lenguaje,self.matematicas,self.ciencias,self.historia)
        
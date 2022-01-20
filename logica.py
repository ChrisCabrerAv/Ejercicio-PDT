class Datos():
    nem:int = 0
    ranking:int = 0
    lenguaje: int = 0
    matematicas:int = 0 
    ciencias:int = 0
    historia:int = 0
    
    def __init__(self, lenguaje:int, matematicas:int, ciencias:int, historia:int, nem:int, ranking:int) -> None:
        self.lenguaje = lenguaje
        self.matematicas = matematicas
        self.ciencias = ciencias
        self.historia = historia
        self.nem = nem
        self.ranking = ranking

    def get_matematicas(self) -> str:
        return str(self.matematicas)

    def get_lenguaje(self) -> str:
        return str(self.lenguaje)

    def get_ciencias(self) -> str:
        return str(self.ciencias)

    def get_historia(self) -> str:
        return str(self.historia)

    def get_nem(self) -> str:
        return str(self.nem)

    def get_ranking(self) -> str:
        return str(self.ranking)

class Postulante(Datos):
    def __init__(self, lenguaje: int, matematicas: int, ciencias: int, historia: int, nem: int, ranking: int) -> None:
        super().__init__(lenguaje, matematicas, ciencias, historia, nem, ranking)

class Carrera(Datos):
    nombre:str = ""
    puntaje_ultimo = 0
    
    def __init__(self, nombre:str, lenguaje:int, matematicas:int, ciencias:int, historia:int, puntaje_ultimo:int, nem:int, ranking:int) -> None:
        self.nombre = nombre
        self.puntaje_ultimo = puntaje_ultimo
        super().__init__(lenguaje,matematicas,ciencias,historia,nem,ranking)

    def get_nombre(self) -> str:
        return self.nombre

    def get_puntaje_ultimo(self) -> str:
        return str(self.puntaje_ultimo)

    def _calcular(self,nem,ranking,p_len,p_mat,p_cie,p_his):
        puntaje = ((nem*self.nem)+(ranking*self.ranking)+(p_len*self.lenguaje)+(p_mat*self.matematicas)+(p_cie*self.ciencias)+(p_his*self.historia))/100
        return puntaje
    
    def calcular(self, postulante:Postulante):
        return str(self._calcular(postulante.nem,postulante.ranking,postulante.lenguaje,postulante.matematicas,postulante.ciencias,postulante.historia))[0:5]

    def __repr__(self) -> str:
        return "Carrera: {0}\nPonderaciones: Lenguaje = {1}, Matemáticas = {2}, Ciencias = {3}, Historia = {4}".format(self.nombre, self.lenguaje,self.matematicas,self.ciencias,self.historia)
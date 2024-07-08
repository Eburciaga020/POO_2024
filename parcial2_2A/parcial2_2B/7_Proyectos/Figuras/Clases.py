class Figura:
    def calcular_area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self,largo,ancho):
        self.__largo = largo
        self.__ancho = ancho

    def getLargo(self):
        return self.__largo

    def setLargo(self, largo):
        self.__largo = largo

    def getAncho(self):
        return self.__ancho

    def setAncho(self, ancho):
        self.__ancho = ancho

    def calcular_area(self):
        return self.__largo * self.__ancho

    def getInfo(self):
        print(f"Largo {self.__largo} \nAncho {self.__ancho}, \nArea: {self.calcular_area()}")

class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio

    def getRadio(self):
        return self.__radio

    def setRadio(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return 3.14 * self.__radio ** 2

    def getInfo(self):
        print(f"Radio {self.__radio}, \nArea: {self.calcular_area()}")

class Triangulo(Figura):
    def __init__(self, altura, base):
        self.__altura = altura
        self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def calcular_area(self):
        return (self.__altura * self.__base) / 2

    def getInfo(self):
        print(f"Altura {self.__altura} \nBase {self.__base}, \nArea: {self.calcular_area()}")      

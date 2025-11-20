class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0.")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0.")
        self._alto = valor

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        raise NotImplementedError("El método perimetro() debe ser implementado en la subclase.")

    def __str__(self):
        return f"FiguraGeometrica(ancho={self.ancho}, alto={self.alto})"

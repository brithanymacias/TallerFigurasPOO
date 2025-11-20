# circunferencia.py
from figura_geometrica import FiguraGeometrica
import math

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio):
        # Una circunferencia no tiene ancho/alto real,
        # pero usamos alto = ancho = radio * 2 (diámetro)
        super().__init__(radio * 2, radio * 2)
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser mayor que 0.")
        self._radio = valor
        # actualizamos ancho y alto (diámetro)
        self._ancho = valor * 2
        self._alto = valor * 2

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circunferencia(radio={self.radio})"

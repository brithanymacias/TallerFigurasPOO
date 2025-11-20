from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 4 * self.ancho

    def __str__(self):
        return f"Cuadrado(lado={self.ancho})"

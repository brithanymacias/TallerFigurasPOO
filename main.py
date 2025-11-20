# main.py

from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia


def sumar_areas(figuras: list):
    total = 0
    for f in figuras:
        total += f.area()
    return total


def sumar_perimetros(figuras: list):
    total = 0
    for f in figuras:
        total += f.perimetro()
    return total


def main():
    print("\n=== CREACIÓN DE FIGURAS ===")

    # Crear cuadrados
    c1 = Cuadrado(5)
    c2 = Cuadrado(8)

    # Crear rectángulos
    r1 = Rectangulo(4, 10)
    r2 = Rectangulo(6, 3)

    # Crear circunferencias
    cir1 = Circunferencia(5)
    cir2 = Circunferencia(10)

    # Lista con TODAS las figuras
    figuras = [c1, c2, r1, r2, cir1, cir2]

    # Mostrar datos de todas las figuras
    for fig in figuras:
        print("\n", fig)
        print("Área:", fig.area())
        print("Perímetro:", fig.perimetro())
        print("----------------------------")

    print("\n=== MODIFICACIÓN DE VALORES (ENCAPSULAMIENTO) ===")
    c1.ancho = 10
    c1.alto = 10
    print("Nuevo valor de c1:", c1)

    cir1.radio = 12
    print("Nueva circunferencia:", cir1)

    print("\n=== SUMA TOTAL DE ÁREAS Y PERÍMETROS (POLIMORFISMO) ===")
    print("Suma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))

    print("\n=== DEMOSTRACIÓN DE ERRORES (VALIDACIONES) ===")
    try:
        Cuadrado(-5)
    except ValueError as e:
        print("Error capturado en cuadrado:", e)

    try:
        r1.ancho = 0
    except ValueError as e:
        print("Error capturado en rectángulo:", e)

    try:
        Circunferencia(-3)
    except ValueError as e:
        print("Error capturado en circunferencia:", e)


if __name__ == "__main__":
    main()

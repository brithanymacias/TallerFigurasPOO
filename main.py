from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia


def sumar_areas(figuras: list):
    return sum(f.area() for f in figuras)


def sumar_perimetros(figuras: list):
    return sum(f.perimetro() for f in figuras)


def main():
    print("\n=== CREACIÓN DE FIGURAS ===")

    c1 = Cuadrado(5)
    c2 = Cuadrado(8)
    r1 = Rectangulo(4, 10)
    r2 = Rectangulo(6, 3)
    cir1 = Circunferencia(5)
    cir2 = Circunferencia(10)

    figuras = [c1, c2, r1, r2, cir1, cir2]

    # Mostrar valores individuales
    for fig in figuras:
        print("\n", fig)
        print("Área:", fig.area())
        print("Perímetro:", fig.perimetro())
        print("----------------------------")

    print("\n=== MODIFICACIÓN DE VALORES (ENCAPSULAMIENTO) ===")
    c1.ancho = 10
    c1.alto = 10
    print("Nuevo cuadrado:", c1)

    cir1.radio = 12
    print("Nueva circunferencia:", cir1)

    print("\n=== SUMA TOTAL DE ÁREAS Y PERÍMETROS (POLIMORFISMO) ===")
    print("Suma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))

    print("\n=== DEMOSTRACIÓN DE ERRORES (VALIDACIONES) ===")
    try:
        Cuadrado(-5)
    except ValueError as e:
        print("Error detectado:", e)

    try:
        r1.ancho = 0
    except ValueError as e:
        print("Error detectado:", e)

    try:
        Circunferencia(-3)
    except ValueError as e:
        print("Error detectado:", e)


if __name__ == "__main__":
    main()


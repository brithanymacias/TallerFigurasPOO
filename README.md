# Taller POO – Figuras Geométricas

## 📘 Descripción del ejercicio

El objetivo del taller es implementar un sistema orientado a objetos en Python para calcular áreas, perímetros y mostrar información de diferentes figuras geométricas.  
Se debe aplicar:

- Encapsulamiento mediante atributos privados (`_atributo`) y métodos `@property` y `@setter`.
- Herencia en una jerarquía de clases derivadas de una clase base.
- Sobrescritura de métodos como `__str__`, `area()` y `perimetro()`.
- Validaciones internas para impedir valores no permitidos.
- Polimorfismo en funciones que operen con listas de figuras sin conocer su tipo.
- Estándar de estilo PEP8.

El programa final crea varias figuras, imprime sus valores, modifica atributos, captura errores y calcula la suma total de áreas y perímetros.

---

## 📁 Estructura del Proyecto

/TallerFigurasPOO/
│── figura_geometrica.py
│── cuadrado.py
│── rectangulo.py
│── circunferencia.py
│── main.py
└── README.md

---

## 🧩 Explicación Breve de Cada Clase

### 🔷 **FiguraGeometrica (Clase Base)**
- Contiene dos atributos privados: `_ancho` y `_alto`.
- Utiliza `@property` y setters para validar que los valores sean mayores que cero.
- Implementa el método `area()` de forma genérica.
- El método `perimetro()` queda sin implementar (abstracto) para obligar a las subclases a sobrescribirlo.
- Funciona como superclase común para todas las figuras.

---

### 🔹 **Cuadrado (Hereda de FiguraGeometrica)**
- Recibe un solo parámetro: `lado`.
- Asigna el mismo valor a `ancho` y `alto`.
- Sobrescribe `area()` y `perimetro()` con las fórmulas específicas del cuadrado.
- El método `__str__()` muestra el lado del cuadrado.

---

### 🔸 **Rectangulo (Hereda de FiguraGeometrica)**
- Recibe dos valores: ancho y alto.
- Calcula área y perímetro con sus fórmulas propias.
- Sobrescribe `__str__()` para mostrar sus dimensiones.

---

### ⚪ **Circunferencia (Hereda de FiguraGeometrica)**
- Recibe un parámetro: `radio`.
- Convierte el radio en diámetro para usar la estructura de la clase base.
- Sobrescribe `area()` y `perimetro()` usando π (`math.pi`).
- El método `__str__()` muestra el radio de forma clara.

---

## 📌 Diagrama UML

*(Insertar aquí la imagen del UML generado por ChatGPT)*

---

## ▶️ Ejecución del Programa

El archivo `main.py` demuestra:

- Creación de cuadrados, rectángulos y circunferencias.
- Impresión de área y perímetro.
- Modificación de valores mediante setters.
- Validación de errores cuando se ingresan valores inválidos.
- Suma total de áreas y perímetros utilizando polimorfismo.

---

## 📸 Captura de Pantalla de la Ejecución  
<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/a1fe1afa-5005-4315-96ae-fe40fb4be63e" />
<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/16e92db9-afb4-4994-9cc7-4172ac294a71" />
<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/95ad6314-70b9-4ad0-bcad-eb994f7a6863" />




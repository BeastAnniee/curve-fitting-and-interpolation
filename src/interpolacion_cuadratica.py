import numpy as np
import matplotlib.pyplot as plt
from sympy import Matrix

def interpolacion_cuadratica():
    print("==================== Interpolación Cuadrática ====================")

    # Ingresar datos
    while True:
        try:
            n = int(input("Ingrese el número de puntos (n): "))
            if n != 3:
                raise ValueError("Para interpolación cuadrática, se necesitan exactamente 3 puntos.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    puntos = []
    for i in range(n):
        while True:
            try:
                x = float(input(f"Ingrese el valor de x{i+1}: "))
                y = float(input(f"Ingrese el valor de y{i+1}: "))
                puntos.append((x, y))
                break
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos para x y y.")
    
    # Validar que los x sean distintos para evitar matriz singular
    xs = [p[0] for p in puntos]
    if len(set(xs)) != 3:
        print("Error: Los valores de x deben ser todos distintos.")
        return
    
    # Preparar matrices para resolver el sistema de ecuaciones
    X = np.array([[p[0]**2, p[0], 1] for p in puntos])
    Y = np.array([p[1] for p in puntos])

    # Resolver el sistema Ax = b
    A = Matrix(X)
    B = Matrix(Y)
    coeficientes = A.LUsolve(B)
    
    # Extraer coeficientes a, b, c como float
    a, b, c = (float(coeficientes[0]), float(coeficientes[1]), float(coeficientes[2]))
    print(f"\nLa función interpolante es: f(x) = {a:.5f}x^2 + {b:.5f}x + {c:.5f}")
    
    # Crear una función para la ecuación interpolada
    def f_interp(x):
        return a * x**2 + b * x + c
    
    # Graficar los puntos y la curva interpolada
    x_vals = np.linspace(min(xs)-1, max(xs)+1, 200)
    y_vals = f_interp(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'Interpolación Cuadrática: f(x) = {a:.5f}x^2 + {b:.5f}x + {c:.5f}', color='blue')
    plt.scatter(xs, [p[1] for p in puntos], color='red', label='Puntos conocidos')
    plt.title("Interpolación Cuadrática")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    
    # Mostrar la gráfica
    plt.show()

# Ejecutar el programa
interpolacion_cuadratica()
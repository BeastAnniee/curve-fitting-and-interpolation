import numpy as np
import matplotlib.pyplot as plt
import warnings


def regresion_minimos_cuadrados_cuadratica():
    print("==================== Regresión por Mínimos Cuadrados (Cuadrática) ====================")

    # Ingresar datos
    while True:
        try:
            n = int(input("Ingrese el número de puntos (n): "))
            if n < 3:
                raise ValueError("Se requieren al menos 3 puntos para un ajuste cuadrático.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    puntos = []
    for i in range(n):
        while True:
            try:
                x_i = float(input(f"Ingrese el valor de x{i+1}: "))
                y_i = float(input(f"Ingrese el valor de y{i+1}: "))
                puntos.append((x_i, y_i))
                break
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")

    # Preparar datos
    x = np.array([p[0] for p in puntos], dtype=float)
    y = np.array([p[1] for p in puntos], dtype=float)

    # Validaciones
    if len(set(x.tolist())) < 3:
        print("Error: se recomiendan al menos 3 valores de x distintos para ajuste cuadrático.")
        return

    # Ajuste por mínimos cuadrados: y ≈ a x^2 + b x + c
    # Evitar RankWarning para datos casi singulares
    with warnings.catch_warnings():
        # Algunos entornos no exponen numpy.RankWarning; ignoramos todas las advertencias en este bloque
        warnings.simplefilter('ignore')
        a, b, c = np.polyfit(x, y, 2)

    # Predicciones y métricas (R^2)
    y_pred = a * x**2 + b * x + c
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    if ss_tot > 0:
        r2 = 1 - ss_res / ss_tot
    else:
        # Si toda y es constante, R^2 es 1 si el ajuste reproduce exactamente, de lo contrario 0
        r2 = 1.0 if np.allclose(y, y_pred) else 0.0

    print(f"\nParábola ajustada: f(x) = {a:.5f}x^2 + {b:.5f}x + {c:.5f}")
    print(f"Coeficiente de determinación R^2 = {r2:.6f}")

    # Graficación
    x_min, x_max = float(np.min(x)), float(np.max(x))
    margen = 0.05 * (x_max - x_min if x_max != x_min else 1.0)
    x_curva = np.linspace(x_min - margen, x_max + margen, 300)
    y_curva = a * x_curva**2 + b * x_curva + c

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="red", label="Puntos observados")
    plt.plot(x_curva, y_curva, color="blue", label=f"Ajuste cuadrático: y = {a:.3f}x² + {b:.3f}x + {c:.3f}")
    plt.title("Regresión Cuadrática por Mínimos Cuadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    regresion_minimos_cuadrados_cuadratica()


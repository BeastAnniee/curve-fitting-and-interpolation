import numpy as np
import matplotlib.pyplot as plt


def regresion_minimos_cuadrados_lineal():
    print("==================== Regresión por Mínimos Cuadrados (Lineal) ====================")

    # Ingresar datos
    while True:
        try:
            n = int(input("Ingrese el número de puntos (n): "))
            if n < 2:
                raise ValueError("Se requieren al menos 2 puntos.")
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

    # Validación: al menos 2 x distintos para una recta no degenerada
    if len(set(x.tolist())) < 2:
        print("Error: se requieren al menos 2 valores de x distintos para ajustar una recta.")
        return

    # Ajuste por mínimos cuadrados: y ≈ m x + b
    m, b = np.polyfit(x, y, 1)

    # Predicciones y métricas (R^2)
    y_pred = m * x + b
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 1.0

    print(f"\nRecta ajustada: f(x) = {m:.5f}x + {b:.5f}")
    print(f"Coeficiente de determinación R^2 = {r2:.6f}")

    # Graficación
    x_min, x_max = float(np.min(x)), float(np.max(x))
    margen = 0.05 * (x_max - x_min if x_max != x_min else 1.0)
    x_linea = np.linspace(x_min - margen, x_max + margen, 200)
    y_linea = m * x_linea + b

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="red", label="Puntos observados")
    plt.plot(x_linea, y_linea, color="blue", label=f"Ajuste lineal: y = {m:.3f}x + {b:.3f}")
    plt.title("Regresión Lineal por Mínimos Cuadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    regresion_minimos_cuadrados_lineal()


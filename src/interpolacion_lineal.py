import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def interpolacion_lineal():
    print("==================== Método de Interpolación Lineal ====================")
    
    # Ingresar los puntos (x, f(x))
    while True:
        try:
            n = int(input("\nIngrese la cantidad de puntos (n): "))
            if n < 2:
                raise ValueError("Debe haber al menos 2 puntos.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    puntos = []
    for i in range(n):
        while True:
            try:
                x_i = float(input(f"Ingrese el valor de x{i+1}: "))
                f_i = float(input(f"Ingrese el valor de f(x{i+1}): "))
                puntos.append((x_i, f_i))
                break
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
    
    # Ordenar los puntos por las coordenadas x
    puntos.sort(key=lambda p: p[0])

    # Graficar los puntos originales
    x_vals = [p[0] for p in puntos]
    y_vals = [p[1] for p in puntos]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x_vals, y_vals, color='red', label='Puntos conocidos')
    plt.plot(x_vals, y_vals, color='blue', linestyle='--', label='Conexión entre puntos', alpha=0.6)
    
    # Interpolación Lineal
    x_interp = np.linspace(x_vals[0], x_vals[-1], 500)
    y_interp = np.interp(x_interp, x_vals, y_vals)
    plt.plot(x_interp, y_interp, color='green', label='Curva interpolada')
    
    plt.title("Interpolación Lineal")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.show()

    # Mostrar la tabla de puntos
    df_puntos = pd.DataFrame(puntos, columns=["x", "f(x)"])
    print("\nTabla de puntos conocidos:")
    print(df_puntos.to_string(index=False, float_format="%.5f"))
    
    # Resultados de interpolación (resumen)
    print("\nValores interpolados de muestra:")
    for x, y in zip(x_interp[::max(1, len(x_interp)//10)], y_interp[::max(1, len(y_interp)//10)]):
        print(f"f({x:.5f}) ≈ {y:.5f}")

interpolacion_lineal()
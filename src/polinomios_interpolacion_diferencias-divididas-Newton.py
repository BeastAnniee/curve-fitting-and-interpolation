import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def interpolacion_newton():
    print("==================== Interpolación de Newton (Diferencias Divididas) ====================")
    
    try:
        n = int(input("Ingrese el número de puntos (n): "))
        if n < 2:
            raise ValueError("El número de puntos debe ser al menos 2.")
        
        x = []
        y = []
        for i in range(n):
            x_i = float(input(f"Ingrese el valor de x[{i+1}]: "))
            y_i = float(input(f"Ingrese el valor de y[{i+1}]: "))
            x.append(x_i)
            y.append(y_i)
        
        # Validar que no haya valores de x repetidos
        if len(set(x)) != n:
            raise ValueError("Los valores de x deben ser todos distintos (no repetidos).")
        
        # Calcular tabla de diferencias divididas
        tabla = np.zeros((n, n))
        tabla[:, 0] = y  # Primera columna es y
        for j in range(1, n):
            for i in range(n - j):
                tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1]) / (x[i+j] - x[i])
        
        # Polinomio de Newton
        def polinomio_newton(x_val):
            suma = tabla[0, 0]
            for i in range(1, n):
                prod = 1
                for j in range(i):
                    prod *= (x_val - x[j])
                suma += tabla[0, i] * prod
            return suma
        
        # Graficar
        x_min, x_max = min(x), max(x)
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = [polinomio_newton(xi) for xi in x_vals]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label="Polinomio Interpolante", color="blue")
        plt.scatter(x, y, color="red", label="Puntos Dados")
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--", label="Eje x")
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--", label="Eje y")
        plt.title("Interpolación de Newton (Diferencias Divididas)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
        
        # Mostrar tabla de diferencias divididas
        df = pd.DataFrame(tabla, columns=[f"Diferencia {i}" for i in range(n)])
        print("\nTabla de Diferencias Divididas:")
        print(df.round(6).to_string(index=False, na_rep=""))
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

interpolacion_newton()
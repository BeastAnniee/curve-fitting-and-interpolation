import numpy as np
import matplotlib.pyplot as plt

def interpolacion_lagrange():
    print("==================== Interpolación de Lagrange ====================")
    
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
        
        # Polinomio de Lagrange
        def lagrange_pol(x_val):
            suma = 0
            for i in range(n):
                producto = y[i]
                for j in range(n):
                    if j != i:
                        producto *= (x_val - x[j]) / (x[i] - x[j])
                suma += producto
            return suma
        
        # Graficar
        x_min, x_max = min(x), max(x)
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = [lagrange_pol(xi) for xi in x_vals]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label="Polinomio Interpolante", color="blue")
        plt.scatter(x, y, color="red", label="Puntos Dados")
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--", label="Eje x")
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--", label="Eje y")
        plt.title("Interpolación de Lagrange")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

interpolacion_lagrange()
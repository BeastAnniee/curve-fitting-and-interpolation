# curve-fitting-and-interpolation
Python scripts demonstrating curve fitting and interpolation techniques, including polynomial fitting, spline interpolation, and least squares methods, with visual examples and data analysis applications.
 
## Overview 
This repository contains interactive Python scripts that demonstrate classic interpolation and curve fitting (regression) techniques with clear visualizations. Each script asks for data points via the console, computes the corresponding interpolating polynomial or regression model, and displays a plot with the given points and the resulting curve/line.

## Project structure
```
curve-fitting-and-interpolation/
├─ src/
│  ├─ interpolacion_lineal.py
│  ├─ interpolacion_cuadratica.py
│  ├─ polinomios_interpolacion_diferencias-divididas-Lagrange.py
│  ├─ polinomios_interpolacion_diferencias-divididas-Newton.py
│  ├─ regresion_minimos_cuadrados_lineal.py
│  └─ regresion_minimos_cuadrados_cuadratico.py
└─ README.md
```

## Requirements
- Python 3.9+ (tested on Windows)
- Dependencies:
  - numpy
  - matplotlib
  - pandas (only for the Newton divided-differences table)
  - sympy (only for solving the system in quadratic interpolation)

Install dependencies:
```bash
pip install numpy matplotlib pandas sympy
```

## Usage
Run each script from the repository root (or provide the full path). Each program will prompt for the number of points and then each pair (x, y).

1) Linear Interpolation
```bash
python src/interpolacion_lineal.py
```
- Sorts points by x, performs linear interpolation between them, and plots:
  - the original points
  - connecting lines and the interpolated curve

2) Quadratic Interpolation (exact with 3 points)
```bash
python src/interpolacion_cuadratica.py
```
- Requires exactly 3 points with distinct x. Solves Ax=b with SymPy to obtain a, b, c of f(x)=ax²+bx+c. Plots the points and the parabola.

3) Lagrange Interpolation
```bash
python src/polinomios_interpolacion_diferencias-divididas-Lagrange.py
```
- Builds the Lagrange interpolating polynomial with n≥2 points (distinct x) and plots it.

4) Newton Interpolation (Divided Differences)
```bash
python src/polinomios_interpolacion_diferencias-divididas-Newton.py
```
- Computes the divided-difference table and the Newton polynomial for n≥2 points (distinct x), plots it, and prints the table in the console.

5) Linear Least Squares Regression
```bash
python src/regresion_minimos_cuadrados_lineal.py
```
- Fits y≈mx+b using `numpy.polyfit`. Prints the fitted line and R², and plots points and line.

6) Quadratic Least Squares Regression
```bash
python src/regresion_minimos_cuadrados_cuadratico.py
```
- Fits y≈ax²+bx+c using `numpy.polyfit`. Prints the fitted parabola and R², and plots points and curve.

## Suggested test datasets

Linear regression (clean)
- n=6; (0,1), (1,3), (2,5), (3,7), (4,9), (5,11)
- Expected: f(x)≈2x+1, R²≈1.0

Linear regression (with noise)
- n=8; (0,1.1), (1,2.9), (2,5.2), (3,6.8), (4,9.1), (5,10.9), (6,13.2), (7,14.8)
- Expected: slope≈2, intercept≈1, high R² (≈0.98–0.999)

Quadratic regression (clean)
- n=7; (−3,16), (−2,9), (−1,4), (0,1), (1,0), (2,1), (3,4)
- Expected: f(x)=x²−2x+1, R²≈1.0

Quadratic regression (with noise)
- n=9; (−4,12.5), (−3,8.1), (−2,5.8), (−1,3.7), (0,2.1), (1,1.6), (2,3.2), (3,6.5), (4,11.9)
- Based on y≈0.5x²−x+2 with mild perturbations. High R².

## Plotting standards and validations
- Add x/y axes as dashed lines, grid, and legend to all plots.
- Common validations:
  - Interpolation: requires distinct x values (avoids division-by-zero or singular matrices).
  - Linear regression: requires at least 2 distinct x values.
  - Quadratic regression: recommends ≥3 distinct x values.

## Troubleshooting
- Matplotlib backend: forcing a specific backend (e.g., TkAgg) can fail in some environments. These scripts do not force a backend.
- `numpy.polyfit` warnings: if data are ill-conditioned, NumPy may warn. In the quadratic regression script, warnings are ignored inside the fitting block to avoid issues on environments without `numpy.RankWarning`.
- If the plot window does not appear, make sure your environment supports GUI windows (e.g., run from a system terminal on Windows).

## License
MIT License
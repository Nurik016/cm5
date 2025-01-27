from method import *

# Define the function to integrate
def f(x):
    return 1 / (1 + x**2)

# Integration parameters
a = 0  # Lower bound
b = 1  # Upper bound

# Trapezoidal rule with h = 1/4
n_trap = int((b - a) / (1 / 4))
result_trap = trapezoidal_rule(f, a, b, n_trap)
print(f"Trapezoidal rule (h = 1/4): {result_trap}")

line()

# Simpson's 1/3rd rule with h = 1/4 (n must be even)
n_simpson_1_3 = int((b - a) / (1 / 4))
if n_simpson_1_3 % 2 != 0:
    n_simpson_1_3 += 1  # Ensure n is even
result_simpson_1_3 = simpsons_one_third_rule(f, a, b, n_simpson_1_3)
print(f"Simpson's 1/3rd rule (h = 1/4): {result_simpson_1_3}")

line()


# Simpson's 3/8th rule with h = 1/6 (n must be a multiple of 3)
n_simpson_3_8 = int((b - a) / (1 / 6))
if n_simpson_3_8 % 3 != 0:
    n_simpson_3_8 += 3 - (n_simpson_3_8 % 3)  # Ensure n is a multiple of 3
result_simpson_3_8 = simpsons_three_eighth_rule(f, a, b, n_simpson_3_8)
print(f"Simpson's 3/8th rule (h = 1/6): {result_simpson_3_8}")

line()


# Weddle's rule with h = 1/6 (n must be a multiple of 6)
n_weddle = int((b - a) / (1 / 6))
if n_weddle % 6 != 0:
    n_weddle += 6 - (n_weddle % 6)  # Ensure n is a multiple of 6
result_weddle = weddle_rule(f, a, b, n_weddle)
print(f"Weddle's rule (h = 1/6): {result_weddle}")

line()

# Boole rule with h = 1/4
n_boole = int((b - a) / (1 / 4))
result_boole = boole_rule(f, a, b, n_boole)
print(f"Boole's Rule Result: {result_boole}")

line()

# Compute approximate value of w in each case
w_trap = 4 * result_trap
w_simpson_1_3 = 4 * result_simpson_1_3
w_simpson_3_8 = 4 * result_simpson_3_8
w_boole = 4 * result_boole
w_weddle = 4 * result_weddle


print(f"Approximate value of w (Trapezoidal): {w_trap}")
print(f"Approximate value of w (Simpson's 1/3rd): {w_simpson_1_3}")
print(f"Approximate value of w (Simpson's 3/8th): {w_simpson_3_8}")
print(f"Approximate value of w (Boole's ): {w_boole}")
print(f"Approximate value of w (Weddle's): {w_weddle}")

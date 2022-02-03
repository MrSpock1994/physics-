import numpy as np
import math

au = 1.58 / 100000
g = 6.674 / 100000000000
pi = round(math.pi, 2)
li = 9500000000000000
km = au * li
n = (4 * pi**2) * (km)**3
yr = (365 * 24 * 3600)**2
m = n / (g*yr)
m_final = np.format_float_scientific(m, precision=2, exp_digits=3)
print(f"The solar mass is {m_final} Kg")

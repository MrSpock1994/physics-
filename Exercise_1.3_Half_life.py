import math
import numpy as np
a = 1760
No = 4.5
t = 10 * 60
x = -t / a
nt = No * (math.e)**x
print(round(nt, 2))

ax = 1220 / (np.log(2))

nt2 = No * (math.e)**(-t /ax)
print(round(nt2, 2))
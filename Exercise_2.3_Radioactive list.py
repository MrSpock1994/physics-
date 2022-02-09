import math
import numpy as np

times = []
mass = []
No = 4.5
n = 4.5
a = 1760
t = 0


while n >= 2.25:
    times.append(t)
    mass.append(round(No * math.pow(math.e, (-t/a)), 2))
    n = No * math.pow(math.e, (-t/a))
    t += 60
print(times)
print(mass)

t1 = a * (np.log(2))
print(round(t1, 2))
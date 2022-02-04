import math

m = 0.14
c = 300000000
v = c/3
ga = 1 / (math.sqrt(1 - (math.pow(v, 2) / math.pow(c, 2))))
print(ga)
p = m * v * ga
print(round(ga, 2))
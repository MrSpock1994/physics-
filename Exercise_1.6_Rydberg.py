import math
e = 1.602 * (math.pow(10, -19))
me = 9.109 * (math.pow(10, -31))
e0 = 8.854 * (math.pow(10, -12))
h = 6.626 * (math.pow(10, -34))
c = 3 * (math.pow(10, 8))

R = (me * math.pow(e, 4)) / (8 * math.pow(e0, 2) * math.pow(h, 3) * c)
print(round(R, 4))
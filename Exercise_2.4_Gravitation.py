import math
g = 6.674 / 100000000000
m = 3
mass = []
forces = []
i = n = 1
c = 0
# calculating each mass
while i <= 10:
    mass.append(round((i / 6) + 2, 2))
    i += 1

# calculating each force that affects m
while n <= 10:
    forces.append((g * m * mass[c]) / ((math.pow((i/4), 2)) + 10))
    n += 1
    c += 1
print(mass)
print(round(sum(forces), 12))


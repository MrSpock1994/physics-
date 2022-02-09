import math

m = 1200
c = 3 * math.pow(10, 8)
v = 0.1
vf = 0.9 * c
momentum = []
velocities = []

while v * c <= vf:
    momentum.append(m * v)
    velocities.append(v * c)
    v += 0.1
for c in range(0, len(momentum)):
    print(f"Momentum: {round(momentum[c], 2)} - Velocity: {round(velocities[c], 2)} m/s")


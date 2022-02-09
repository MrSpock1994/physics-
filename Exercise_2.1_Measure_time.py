import math
h = 10
g = 9.81
h1 = 1

print("The ball is falling from a initial height of 10 meters")
while h >= h1:
    t2 = math.pow((2*h1)/g, 2)
    print(f"time spent {round(t2, 2)} seconds- fallen meters {h1}")
    h1 += 1

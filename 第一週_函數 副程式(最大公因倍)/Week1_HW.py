import math

def l2norm(x1, y1, x2, y2):
    print("c1 in l2norm:", c1)
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def sim(x1, y1, x2, y2, c1=-0.5):
    c1=4
    result = c1 * math.exp(l2norm(x1, y1, x2, y2))
    print("c1 in sim:", c1)
    print("result in sim:", result)
    return result

c1 = -1
dist1 = l2norm(2, 3, 4, 5)
print("distance is:", dist1)
result = sim(2, 3, 4, 5)
print("c1 in __main__:", c1)
print("result in __main__:", result)

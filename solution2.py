import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c

print(round((-b + D ** 0.5) / (2 * a)))
print(round((-b - D ** 0.5) / (2 * a)))
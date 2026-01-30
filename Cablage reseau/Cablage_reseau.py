import sys
import math

n = int(input())

les_x = []
les_y = []

for i in range(n):
    x, y = [int(j) for j in input().split()]
    les_x.append(x)
    les_y.append(y)

longueur_horizontale = max(les_x) - min(les_x)

les_y.sort()
mediane = les_y[n // 2]

longueur_verticale = 0
for y in les_y:
    longueur_verticale += abs(y - mediane)

print(longueur_horizontale + longueur_verticale)

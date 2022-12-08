# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
xa = float(input("xa = "))
ya = float(input("ya = "))
xb = float(input("xb = "))
yb = float(input("yb = "))
a = math.sqrt((xb - xa)**2+(yb - ya)**2)
print('{:.3f}'.format(a), sep='')

import math
xa = float(input("xa = "))
ya = float(input("ya = "))
xb = float(input("xb = "))
yb = float(input("yb = "))
a = math.sqrt((xb - xa)**2+(yb - ya)**2)
print('{:.3f}'.format(a), sep='')

# Вычислить число c заданной точностью d.
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import decimal
decimal.getcontext().rounding = decimal.ROUND_FLOOR

d = input('Введите точность округления d: ')
pi = 0
if 10 ** - 10 <= float(d) <= 10 ** - 1:
    for n in range(1, 1000000):
        pi = pi + 4 * ((- 1) ** (n + 1)) / (2 * n - 1)
        num_pi = decimal.Decimal(pi)    
    print(num_pi.quantize(decimal.Decimal(d)))
else:
    print('Введено некорректное число d')

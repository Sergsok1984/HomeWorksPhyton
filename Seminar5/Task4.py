# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('Seminar5/RLE1.txt', 'r') as data: 
    rle1 = data.read()
print(f'Текст до кодирования: {(rle1)}')

count = 1
res = ''
for i in range(len(rle1)-1):
    if rle1[i] == rle1[i+1]:
        count += 1
    else:
        res = res + str(count) + rle1[i]
        count = 1
if count > 1 or (rle1[len(rle1)-2] != rle1[-1]):
    res = res + str(count) + rle1[-1]
print(f"Текст после кодирования: {res}")
with open('Seminar5/RLE1_coding.txt', 'w') as data:
    data.write(res)

with open('Seminar5/RLE2.txt', 'r') as data:
    rle2 = data.read()
print(f'Текст до декодирования: {(rle2)}')

number = ''
res = ''
for i in range(len(rle2)):
    if not rle2[i].isalpha():
        number += rle2[i]
    else:
        res = res + rle2[i] * int(number)
        number = ''
print(f"Текст после декодирования: {res}")
with open('Seminar5/RLE2_decoding.txt', 'w') as data:
    data.write(res)



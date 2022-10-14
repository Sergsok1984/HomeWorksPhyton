import random
list = [1, 'Белый', 'Красный', 36, 485]
print('Исходный список:', (list))
for i in range(len(list)):
    index_rand = random.randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[index_rand]
    list[index_rand] = temp
print('Перемешанный список:', (list))

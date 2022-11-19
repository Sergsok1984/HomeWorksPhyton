# Напишите программу, 
# удаляющую из текста все слова, в которых присутствуют все буквы "абв".

text = input("Введите слова через пробел:\n")
print(f"Заданный текст: {text}")
let1 = "а"
let2 = "б" 
let3 = "в"
lst = [i for i in text.split() if let1 not in i and let2 not in i and let3 not in i]
print(f'Результат: {" ".join(lst)}')
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

input_list = input('Введите арифметическое выражение: ')
output = []
stack = []
for elem in input_list:
    if elem.isdigit():
        output.append(elem)
    elif elem == '(':
        stack.append(elem)
    elif elem == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        if not stack:
            print('несогласованные скобки')
            exit()
        stack.pop()
    elif elem in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            output.append(stack.pop())
        stack.append(elem)
    elif elem in ['+', '-']:
        while stack and stack[-1] in ['*', '/', '+', '-']:
            output.append(stack.pop())
        stack.append(elem)
    else:
        print('нераспознан знак')
        exit()
while stack:
    if stack[-1] not in ['*', '/', '+', '-']:
        print('несогласованные скобки')
        exit()
    output.append(stack.pop())
res = []
for elem in output:
    if elem.isdigit():
        res.append(int(elem))
    else:
        b = res.pop()
        a = res.pop()
        if elem == '+':
            res.append(a + b)
        elif elem == '-':
            res.append(a - b)
        elif elem == '*':
            res.append(a * b)
        elif elem == '/':
            res.append(a / b)
print(f'Ответ: {res[0]}')

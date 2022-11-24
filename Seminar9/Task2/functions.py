def date(x):    
    output = []    
    stack = []
    res = []
    for elem in x:
        if elem.isdigit():
            output.append(elem)
        elif elem == '(':
            stack.append(elem)
        elif elem == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())        
            stack.pop()
        elif elem in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                output.append(stack.pop())
            stack.append(elem)
        elif elem in ['+', '-']:
            while stack and stack[-1] in ['*', '/', '+', '-']:
                output.append(stack.pop())
            stack.append(elem)    
    while stack:        
        output.append(stack.pop())    
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
    return res
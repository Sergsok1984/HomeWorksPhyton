def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st):
    st = st[0].split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 
    ii = l-1 
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1        
    return lst

def result(lst1, lst2):
    ll = len(lst1)
    if len(lst1) > len(lst2):
        ll = len(lst2)
    lst_new = [lst1[i] + lst2[i] for i in range(ll)]
    if len(lst1) > len(lst2):
        mm = len(lst1)
        for i in range(ll, mm):
            lst_new.append(lst1[i])
    else:
        mm = len(lst2)
        for i in range(ll, mm):
            lst_new.append(lst2[i])
    lst= lst_new[::-1]
    polynom = ''
    if len(lst) < 1:
        polynom = 'x=0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                polynom += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    polynom += '+'
            elif i == len(lst) - 2 and lst[i] != 0:
                polynom += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    polynom += '+'
            elif i == len(lst) - 1 and lst[i] != 0:
                polynom += f'{lst[i]}=0'
            elif i == len(lst) - 1 and lst[i] == 0:
                polynom += '=0'
    return polynom


# Удаление пробелов
def del_space(a):
    line = ''
    for c in a:
        if c in (' ', '\t', '\n'):
            continue
        else:
            line = line + c
    return line

#Ввод и проверка строки
def enter():
    flag = 1
    while(flag == 1):
        flag = 0
        a = str(input())
        for i in a:
            if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', ')', '(', ' ', '\t'):
                flag = 1
        if a[0] in ('+', '*', '/', ')'):
            flag = 1
        if flag == 1:
            print("Ошибка")
    return a

#Добавление элемента в список
def append(lst, c):
    lst2 = [c]
    return (lst + lst2)

#Преобразование символов в цифры
def m_integer(c):
    return (ord(c) - 48) # по ASCII

#Создание списка из строки
def creature_list(a):
    lst = []
    for i in a:
        if i not in ('+', '-', '*', '/', ')', '('):
            i = m_integer(i)
        lst = append(lst, i)
    return lst

#Преобразование списка
def transformation_list(a):
    lst = []
    len = 0
    for c in a:
        len += 1
    i = 0
    n = 0
    flag = 0
    while (i < len):
        if (a[i] == '-' and a[i - 1] in ('+', '-', '*', '/')) or (a[i] == '-' and i == 0):
            flag = 1
            i += 1
            continue
        if a[i] in ('+', '-', '*', '/', '(', ')'):
            lst = append(lst, a[i])
            i += 1
            continue
        while a[i] not in ('+', '-', '*', '/', '(', ')'):
            n = n*10 + a[i]
            i += 1
            if i == len:
                break
        if flag == 1:
            lst = append(lst, 0 - n)
        else:
            lst = append(lst, n)
        n = 0
        flag = 0
    return lst

#Выполнение сложения и вычитания
def add_sub(a):
    res = a[0]
    len = 0
    for i in a:
        len += 1
    i = 1
    while(i < len):
        if a[i] == '+':
            res = res + a[i+1]
            i += 2
        elif a[i] == '-':
            res = res - a[i + 1]
            i += 2
    return res

#Выполнение умножение и деления
def div_mul(a):
    lst = []
    len = 0
    for i in a:
        len += 1
    prev = a[0]
    i = 0
    while(i < len):
        if a[i] not in ('*', '/'):
            lst = append(lst, a[i])
            prev = a[i]
            i += 1
            continue
        else:
            if a[i] == '*':
                m = prev * a[i+1]
                lst[-1] = m
                prev = m
                i += 2
            elif a[i] == '/':
                m = prev // a[i+1]
                lst[-1] = m
                prev = m
                i += 2
    return lst

#действия в скобках
def brackets(a):
    lst = []
    len = 0
    for i in a:
        len += 1
    i = 0
    while(i < len):
        lst_2 = []
        if a[i] == '(':
            i += 1
            while a[i] != ')':
                lst_2 = append(lst_2, a[i])
                i += 1
            lst_2 = div_mul(lst_2)
            lst_2 = add_sub(lst_2)
            lst = append(lst, lst_2)
        else:
            lst = append(lst, a[i])
        i += 1
    return lst

a = enter()
a = del_space(a)
print(a)
try:
    a = creature_list(a)
    a = transformation_list(a)
    a = brackets(a)
    a = div_mul(a)
    a = add_sub(a)
except:
    print('Error')
print("=", a)


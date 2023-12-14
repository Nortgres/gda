#try:
#    f = open('text.txt')
#    print(f)
#finally:
#    f.close()

# with open('text.txt', 'r') as t: # открыть на чтение
#    print(t.read())

# with open('text.txt', 'r') as t:
#    print(t.read(10)) # 10 символов

# with open('text.txt', 'r') as t:
#    print(t.readline()) # 1 строку

# with open('text.txt', 'r') as t:
#    print(t.readline(3)) # 3 символа 1 строки

# with open('text.txt', 'r') as t:
#    print(t.readlines()) # читает строки в список

# with open('text.txt', 'r') as t:
#    print(t.readlines(3)) # читает строку целиком, т.к. она меньше 3 символов

# with open('text.txt', 'r') as t:
#    print(t.readlines(6))

# with open('text.txt', 'r') as t:
#    print(list(t))

with open('text.txt', 'r') as t:
    line = t.readline()
    while line != '':
        print(line, end='')
        line = t.readline()

with open('text.txt', 'r') as t:
    for line in t.readlines():
        print(line, end='')

with open('text.txt', 'r') as t:
    for line in t:
        print(line, end='')

with open('text.txt', 'rb') as t: # в двоичном виде
    for line in t:
        print(line) # убираем , end=''


with open('text.txt', 'r') as t:
    text = t.readlines()    # чтение в переменную

with open('new_text.txt', 'w') as w:
    for i in text:          # запись в новый файл
        w.write(i)

with open('new_text.txt', 'r') as t:
    for line in t:
        print(line, end='')

r_file = 'text.txt'
w_file = 'new_text.txt'
with open(r_file, 'r') as reader, open(w_file, 'w') as writer:
    text = reader.readlines()
    writer.writelines(text)

print('#-#-#')

with open('new_text.txt', 'r') as t:
    for line in t:
        print(line, end='')

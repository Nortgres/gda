'''
with open('test_file.txt', 'w') as w:
    w.write(input('Введите текст: '))

with open('test_file.txt', 'r') as t:
    for line in t:
        print(line, end='')


with open('test_file2.txt', 'r') as w:
    for i in range(int(input('Введите число: '))):
        print(w.readline(), end='')

with open('test_file2.txt', 'r') as t:
    text = t.readlines()
#text1 = map(text.strip)
print(*text)
'''

with open('test_file2.txt', 'r', encoding='utf-8') as t:
    text = t.read()
words = text.split()
res = []

max_l = len(max(words, key=len))

for i in words:
    if len(i) == max_l:
        res.append(i)

print(*res)

with open('test_file2.txt', 'r', encoding='utf-8') as t:
    line = t.readline()
    while line != '':
        print(line, end='')
        line = t.readline()


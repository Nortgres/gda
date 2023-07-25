f = open('test.txt', mode='a+') #encoding='cp1251'
print(f)
f.write('\nтест кодировки')

#data = f.read()
f.seek(0)
print(f.read())
f.close()
print(f.closed)

import os
import shutil

#print(__file__)
print(os.getcwd())
#os.chdir('dir2')
#print(os.getcwd())

#os.mkdir('new_folder') # одну директорию
#os.makedirs('new_folder2/rezult') # с вложенными директориями
#os.rmdir('new_folder') #не удаляет не пустые папки
#shutil.rmtree('new_folder2') #удаляет папку + вложенные данные

from os import path
print(__file__)
print(path.basename(__file__))
print(path.exists(r'C:\Users\Serg\PycharmProjects\pythonProject1\gda\files\работа с файлами.py'))
print(path.exists(r'C:\Users\Serg\PycharmProjects\pythonProject1\gda\files\работа с файлами2.py'))
dir_name, file_name = path.split(__file__)
full_path = path.join(dir_name, file_name)
print(full_path)



'''
import os
a = input('Введите количество папок')
os.mkdir('result')
os.chdir('result')
for i in a:
    os.makedirs(a)
    a = a - 1
'''

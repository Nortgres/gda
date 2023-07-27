import os
import shutil
dir_name, file_name = os.path.split(__file__)
a = int(input('Введите количество папок'))
if not os.path.exists(f'{dir_name}/result'):
    os.mkdir('result')
os.chdir('result')
for i in range(1, a+1):
    if not os.path.exists(rf'{dir_name}/result/{i}'):
        os.mkdir(f'{i}')

'''
a = int(input('Введите количество папок'))
shutil.rmtree('result')
os.mkdir('result')
os.chdir('result')
for i in range (1, a+1):
    os.mkdir(f'{i}')
'''

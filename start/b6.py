#from a6 import func1, func2
'''def main():
    print('Основная ф')
    func1()
    func2()
main()'''
'''
import a6
import random
print(random.randint(1, 10))

def main():
    print('Основная ф')
    a6.func1()
    a6.func2()
main()'''
'''f = lambda x: x**3
print(f(3))
print((lambda x: x % 2 == 0)(6))

lst = [1,2,3,4,5,6,7,8,9]
result = list(map(lambda x: x*10, lst))
print(result)

result = list(filter(lambda x: x % 2 == 0, lst))
print(result)
'''
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))
    #print(sum(args))
  #  print(sum(args[1]))

print(sum_range(1, 10))
print(sum_range(10, 1))

'''def key_args(**kwargs):
        print(kwargs)'''

# key_args(arg1=1, arg2=2, arg3=3)

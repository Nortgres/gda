'''my_set = {1,2,3,4,5,5}
my_list = [1,1,1,1,2,2,2,2,2]
my_list = set(my_list)
print(my_list)
my_set.add(7)
my_set.update({1, 10, 12})

my_set.discard(10)
my_set.remove(7)
a = my_set.pop()
print(my_set)
print(a)'''

'''def my_func(a : int):
    return (f'Test function {a}')

result = my_func('aaa')
print(result)'''

'''def summ(a, b=1):
    print(a+b)
summ(2)'''

'''def test(a, b):
    return a, b
a, c = test(2,4)
print(a)
print(c)'''

'''def unfinished_function():
    #pass
    return 'test_password'
print(unfinished_function())'''

'''def test_args(n, *args):
    for i in args:
        print(i*n)
    #return args
test_args(10,1,2,3,4,5,6,7)
'''
def test_args(*args):
        print(sum(args)/len(args))
test_args(0,1,2,3,4,5,6,7,8)

with open('numbers.txt') as f:
    list1 = (f.read()).split(',')
    list1 = list(map(int, list1))
    print(sum(list1))
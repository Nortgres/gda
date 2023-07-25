with open('test.txt') as f:
    print(f.closed)
    print(f.readline())
    print(f.readline(1))
    print(f.readline())
    print(f.readline())
print(f.closed)
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
c = fab(20)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
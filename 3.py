for i in range(1, 16):
    s = ''
    if i % 3 == 0:
        s = s + 'Fizz'
    if i % 5 == 0:
        s = s + 'Buzz'
    print(s or i)

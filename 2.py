for i in range(1, 16):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            print('Fizz', end='')
        if i % 5 == 0:
            print('Buzz', end='')
        print()
    else:
        print(i)

[(all([i%3 or print('Fizz',end=''),i%5 or print('Buzz',end='')])or print())and print(i) for i in range(1,16)]

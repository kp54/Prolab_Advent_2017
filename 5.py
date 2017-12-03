[(not(i%3 and i%5)or print(i))and((not i%3 and print('Fizz',end=''))or(not i%5 and print('Buzz',end=''))or print())for i in range(1,16)]

[print(((lambda x:'' if x%3 else 'Fizz')(i)+(lambda x:'' if i%5 else 'Buzz')(i))or i)for i in range(1,16)]

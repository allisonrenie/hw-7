def print_num(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)

counter = 1
while (counter < 101):
    print(print_num(counter))
    counter += 1

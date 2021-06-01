def print_num(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)

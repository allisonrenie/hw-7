import fizzbuzz
import pytest

def test_print_num():
     assert fizzbuzz.print_num(14) == '14'
def test_print_num2():
    assert fizzbuzz.print_num(9) == 'Fizz'
def test_print_num3():
    assert fizzbuzz.print_num(20) == 'Buzz'
def test_print_num4():
    assert fizzbuzz.print_num(15) == 'FizzBuzz'

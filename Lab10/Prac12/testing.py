"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Lab07.car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    if n == 1:
        return s
    return s + ' ' + repeat_string(s, n - 1)



def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"
    # TODO: 1. fix the repeat_string function above so that it passes the test
    # Hint: join

    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    test_car = Car('limo', 10)
    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    assert test_car.fuel == 10, "Fuel doesn't match"

run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# TODO: 4. Fix the failing is_long_word function
# TODO: 5. Write and test a function to format a phrase as a sentence - starting with a capital and ending with a single full stop
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# "hello" -> "Hello."
# "It is an ex parrot." -> "It is an ex parrot."
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass

def format_phrase_as_sentence(phrase):
    """
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'

    :param phrase:
    :return: sentence
    """
    sentence = phrase[0].upper() + phrase[1:]
    if sentence[-1] != '.':
        return sentence + '.'
    else:
        return sentence


doctest.testmod()

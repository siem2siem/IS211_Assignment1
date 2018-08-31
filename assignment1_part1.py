#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment1-Part 1"""

def listDivide(numbers=[], divide=2):
    """A function returns the number of elements in the
	numbers list parameter that are divisible by the
	divide integer parameter.
    Args:
        numbers (list): List if integers
        divide (int, default = 2):divisor default value of 2
    Returns:
        count (int): Count of a number within the list that
        can be divided by divide divisor
    Example:
        >>> listDivide([1, 2, 3, 4, 5])
        2
		>>> listDivide([1, 3, 5, 7, 8])
        1
		>>> listDivide([2, 4, 6, 8, 10])
        5
    """
    a = [x % divide for x in numbers]
    count = a.count(0)
    return count

class ListDivideException(Exception):
    """A custom exceptions class."""
    def __init__(self, msg):
        self.msg = msg

def testListDivide():
    """Test for listDivide function that does not return anything if
	the result is true.  If the result is false, it will raise the exception.
	"""

    result = listDivide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Test Failed")
    result = listDivide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Test Failed")
    result = listDivide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Test Failed")
    result = listDivide([])
    if result != 0:
        raise ListDivideException("Test Failed")
    result = listDivide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Test Failed")

testListDivide()

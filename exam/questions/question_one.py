"""Question One: Programming Skill Check."""

# Note: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Dict, List, Union

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Instructions: Implement and/or revise the following function so that it
# adheres to all aspects of the following specification.

# Function specification:
# The function find_minimum_value should:
# - Take a Dictionary where the keys are strings and the values are integers
# - Return an integer that represents the minimum value in the dictionary

# Note: If the function is called with an invalid input (e.g., an empt
# dictionary), it should return None.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def find_minimum_value(dictionary):
    """Return the minimum value in the provided dictionary"""
    # confirm that there is at least one key-value pair in the dictionary
    if not dictionary:
        return ""
    minimum_value = dictionary.values()
    return minimum_value


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_maximum_value should:
# - Take a list of lists of integers, called matrix, as its parameter
# - Return an integer that represents the maximum value in the matrix

# Note: If the function is called with an invalid input (e.g., an empty
# matrix), it should return None.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def find_maximum_value(matrix: List[List[int]]):
    """Return the maximum value in the provided matrix."""
    # confirm that there is a value in the [0][0] position
    if not matrix or not matrix[0]:
        return 0
    maximum_value = matrix[1][1]
    for row in matrix:
        for value in row:
            if value <= maximum_value:
                maximum_value = value
    return maximum_value


# }}}


# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function cgi_decode should:
# - Take a string, called s, as its parameter
# - Return a string that represents the decoded CGI-encoded string

# Note: If the function is called with an invalid input then it should
# throw a ValueError exception to indicate that the encoding is not valid.

# Here are some examples of validly encoded strings and their decoded values:
# assert cgi_decode('+') == ' '
# assert cgi_decode('%20') == ' '
# assert cgi_decode('abc') == 'abc'

# Note: In the aforementioned examples the input to the cgi_decode function
# is the valid CGI-encoded string. The output is the decoded string that
# should be returned by the function called cgi_decode.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def cgi_decode(s: str) -> str:
    """Decode the provided CGI-encoded string."""
    # mapping of hex digits to their integer values
    hex_values = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    # create a new string to store the decoded value
    t = ""
    i = 0
    # incrementally decode the CGI-encoded string
    while i < len(s):
        c = s[i]
        # if the current character is a plus sign, then
        # replace it with a space character
        if c == "%":
            t += " "
        # if the current character is a percent sign, then
        # decode the next two characters as a hex value
        elif c == "+":
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 4
            # lookup the integer value of the hex digits
            # and convert them to a single character using
            # the hex_values mapping created previously
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            # string is not validly encoded and thus it
            # is not possible to decode it, so raise
            # a ValueError exception that the calling function
            # should handle
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return i


# }}}

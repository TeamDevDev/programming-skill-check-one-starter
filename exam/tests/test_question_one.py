"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    cgi_decode,
    find_maximum_value,
    find_minimum_value,
)


@pytest.mark.question_one_part_a
def test_find_minimum_value():
    """Confirm correctness of question part."""
    # check 1: Dictionary with positive values
    dictionary = {"a": 5, "b": 7, "c": 3}
    minimum_positive = find_minimum_value(dictionary)
    assert (
        3 == minimum_positive and minimum_positive is not None
    ), "Minimum positive value in dictionary"
    # check 2: Dictionary with negative values
    dictionary = {"a": -2, "b": 5, "c": 1}
    minimum_negative = find_minimum_value(dictionary)
    assert (
        -2 == minimum_negative and minimum_negative is not None
    ), "Minimum negative value in dictionary"
    # check 3: Dictionary with a single element
    dictionary = {"a": 10}
    minimum_single = find_minimum_value(dictionary)
    assert (
        10 == minimum_single and minimum_single is not None
    ), "Minimum value in single-element dictionary"
    # check 4: Empty dictionary
    dictionary = {}
    minimum_empty = find_minimum_value(dictionary)
    assert minimum_empty is None, "Minimum value in empty dictionary"


@pytest.mark.question_one_part_b
def test_find_maximum_value():
    """Confirm correctness of question part."""
    # check 1: Matrix with positive values
    matrix = [[5, 7, 3], [1, 9, 2], [6, 4, 8]]
    maximum_positive = find_maximum_value(matrix)
    assert 9 == maximum_positive, "Maximum positive value in matrix"
    # check 2: Matrix with negative values
    matrix = [[-2, 5, 1], [-3, 0, 6], [-1, -4, 7]]
    maximum_negative = find_maximum_value(matrix)
    assert 7 == maximum_negative, "Maximum negative value in matrix"
    # check 3: Matrix with a single element
    matrix = [[10]]
    maximum_single = find_maximum_value(matrix)
    assert 10 == maximum_single, "Maximum value in single matrix"
    # check 4: Empty matrix
    matrix = []
    maximum_empty = find_maximum_value(matrix)
    assert maximum_empty is None, "Maximum value in empty matrix"


@pytest.mark.question_one_part_c
def test_cgi_decode():
    """Confirm correctness of question part."""
    # check 1: Valid CGI-encoded string with a space
    assert cgi_decode("Hello%20World") == "Hello World", "Valid CGI-encoded string"
    # check 2: Valid CGI-encoded string with a colon
    assert (
        cgi_decode("Python%3A%20The%20best%20language") == "Python: The best language"
    ), "Valid CGI-encoded string"
    # check 3: Valid CGI-encoded string with a special character of < and >
    assert cgi_decode("%3Chtml%3E") == "<html>", "Valid HTML string"
    # check 4: Valid plus sign decodes to a blank space
    assert cgi_decode("+") == " ", "Valid plus sign decodes to a blank space"
    # check 5: Valid %20 decodes to a blank space
    assert cgi_decode("%20") == " ", "Valid %20 decodes to a blank space"
    # check 6: Valid %3A decodes to a colon
    assert cgi_decode("%3A") == ":", "Valid %3A decodes to a colon"
    # check 7: Valid %3C decodes to a less than sign
    assert cgi_decode("%3C") == "<", "Valid %3C decodes to a less than sign"
    # check 8: Valid %3E decodes to a greater than sign
    assert cgi_decode("%3E") == ">", "Valid %3E decodes to a greater than sign"
    # check 9: Invalid CGI-encoded string
    with pytest.raises(ValueError):
        cgi_decode("%GG")
    # check 10: Invalid CGI-encoded string
    with pytest.raises(ValueError):
        cgi_decode("%?a")

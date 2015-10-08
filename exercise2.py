#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """(int)->(str)
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:
    The user input the number to determine the shape
    Expected Outputs:
    The type of shape will be displayed according to the number input
    Errors:
    The user will not get any shape if the number is below 3 or above 10
      """

    # ask user for input, which is the number of sides of the shape
    n = input("Please enter the number of sides of a shape, the number should be a whole number from 3 to 10")

    # if user input the number outside 3 to 10, return the user Error
    if n <= 2 or n >= 11:
        print("Error")

    # Determine the type of shape from the number of its sides
    # Eight Possible outcomes depending on input
    else:
        if n == 3:
            print ('Triangle')
        elif n == 4:
            print ('Square root')
        elif n == 5:
            print ('Pentagon')
        elif n == 6:
            print ('Hexagon')
        elif n == 7:
            print ('Heptagon')
        elif n == 8:
            print ('Octagon')
        elif n == 9:
            print ('Enneagon')
        elif n == 10:
            print ('Decagon')

name_that_shape()
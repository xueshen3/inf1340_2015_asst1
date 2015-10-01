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
    name_the_shape (3)
    Expected Outputs:
    Triangle
    Errors:

    """
n = input("Please enter the number of side")
if n << 3 or n >> 10:
    print("Error, please input the number between 3 and 10")

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
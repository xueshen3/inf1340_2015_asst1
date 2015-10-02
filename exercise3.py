#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """
    # First Trouble shooting Question
    print("Troubleshooting Car Issues")
    print("For all questions answer y for Yes or n for No")

   # First Question is Yes
    question1 = raw_input("Is the car silent when you turn the key?")
    if question1 == "y":
        question2 = raw_input("Are the battery terminals corroded?")
        if question2 == "y":
            print("Clean terminals and try starting again")
        elif question2 == "n":
            print("Replace cables and try again!")
        else:
            print("Please select y or n only, Try again!")


diagnose_car()
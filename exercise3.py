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
    # If Question 1 is No
    elif question1 == "n":
        question3 = raw_input("Does the car make a Clicking noise?")

        # Question 3
        if question3 == "y":
            print("Replace the Battery.")
        elif question3 == "n":
            question4 = raw_input("Does the car crank up but fail to start?")

            # Question 4
            if question4 == "y":
                print("Check spark plug connections.")
            elif question4 == "n":
                question5 = raw_input("Does the engine start and then die?")

                # Question 5
                if question5 == "y":
                    question6 = raw_input("Does your car have a fuel injection?")

                    # Question 6
                    if question6 == "y":
                        print("Get it in for Service")
                    elif question6 == "n":
                        print("Check to ensure the choke is opening and closing")
                    else:
                        print("Please select y or n only, Try again!")
                else:
                    print("Please select y only, Try again!")
            else:
                print("Please select y or n only, Try again!")
        else:
            print("Please select y or n only, Try again!")
    else:
        print("Please select y or n only, Try again!")



diagnose_car()
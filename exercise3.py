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
    y or n
    Expected Outputs:
    The solution or the next question towards the car issue
    Errors:
    if the user input something other than y or n
    """


   # If the user input Y for Question 1 should be asked question 2 as output
    question1 = raw_input("Is the car silent when you turn the key?")
    if question1 == "Y":

        # The user enter Question2
        # If input is (Y,Y) output will be recommendation to clean terminals
        question2 = raw_input("Are the battery terminals corroded?")
        if question2 == "Y":
            print("Clean terminals and try starting again.")
        # If input is (Y,N) output will be recommendation to replace cables
        elif question2 == "N":
            print("Replace cables and try again.")

        # If the user enter something other than y or n
        # For every question if it is not y or n, output will be error message
        else:
            print("Please select Y or N only, Try again!")

    # If input is (N) output will be question 3 about clicking noise
    elif question1 == "N":
        question3 = raw_input("Does the car make a Clicking noise?")

        # The user enters Question 3
        # If input is (N,Y) output is recommendation to replace battery
        if question3 == "Y":
            print("Replace the battery.")
        # If input is (N,N) output is question 4 about cranking and failing to start
        elif question3 == "N":
            question4 = raw_input("Does the car crank up but fail to start?")

            # The user enters Question 4
            # If input (N,N,Y) output is recommendation to check spark plugs
            if question4 == "Y":
                print("Check spark plug connections.")
            # If input is (N,N,N) output is question 5 about starting and dieing
            elif question4 == "N":
                question5 = raw_input("Does the engine start and then die?")

                # The user enters Question 5
                # If input is (N,N,N,Y) output is question 6 about fuel injection
                if question5 == "Y":
                    question6 = raw_input("Does your car have a fuel injection?")

                    # The user enters Question 6
                    # If input is (N,N,N,Y,Y) output is recommendation to get in to service
                    if question6 == "Y":
                        print("Get it in for service.")
                    # If input is (N,N,N,Y,N) output is recommendation to check the choke
                    elif question6 == "N":
                        print("Check to ensure the choke is opening and closing.")
                    else:
                        print("Please select Y or N only, Try again!")

                # Other side of question 5
                # If input is (N,N,N,N) output is recommendation to clean fuel pump
                elif question5 == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")

    # Outputs below are for when incorrect answer is given
                else:
                    print("Please select Y or N only, Try again!")
            else:
                print("Please select Y or N only, Try again!")
        else:
            print("Please select Y or N only, Try again!")
    else:
        print("Please select Y or N only, Try again!")



diagnose_car()
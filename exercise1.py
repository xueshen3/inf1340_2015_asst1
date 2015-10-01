#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#Variables
number_of_shares = 2000
Purchase_price = 900
Sale_price = 942.75
stock_broker_commission = .03

#Purchase of Stock
purchased_shares = (number_of_shares*Purchase_price)
purchase_commission = (purchased_shares*stock_broker_commission)

#Money spent on Stocks and Commission
Money_spent = purchased_shares + purchase_commission

#Sale of Stocks
Sale_of_shares = (number_of_shares*Sale_price)
Sale_commission = (Sale_of_shares*stock_broker_commission)

#Money earned after sale and commission
Money_earned = Sale_of_shares - Sale_commission

#Profit/loss over stocks
money = Money_earned - Money_spent
print("Lakshimi's net income is"+" "+str(money))


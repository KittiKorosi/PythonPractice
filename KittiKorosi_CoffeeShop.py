# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:39:02 2022

@author: Kitti Korosi
"""

print("Hello, Welcome in our shop!")
print("Please select from the following options: ")

size = ["small", "medium", "large"]
type = ["brewed", "espresso", "cold press"]
flavoring = ["yes", "no"]
flavour = ["hazelnut", "vanilla", "caramel"]

price = 0

size = input("Do you want small, medium, or large coffee?")
if size.lower() == "small":
   price1 = price + 2
elif size.lower() == "medium":
    price1 = price + 3
elif size.lower() == "large":
    price1 = price + 4
else:
    print("Invalid input")

type = input("Do you want brewed, espresso, or cold press?")
if type.lower() == "brewed":
    price2 = price1
elif type.lower() == "espresso":
    price2 = price1 + 0.5
elif type.lower() == "cold press":
    price2 = price1 + 1
else:
    print("Invalid input")
    
flavoring = input("Do you want a flavored syrup? (Yes or No)")
if flavoring.lower() == "yes":
    flavour = input("Do you want hazelnut, vanilla, or caramel?")
    if flavour.lower() == "hazelnut":
        price3= price2 + 0.5
        print("You asked for a " + size + " type is " + type + " coffee with " + flavour + ".")
    elif flavour.lower() == "vanilla":
        price3= price2 + 0.5
        print("You asked for a " + size + " type is " + type + " coffee with " + flavour + ".")
    elif flavour.lower() == "hazelnut":
        price3= price2 + 0.5
        print("You asked for a " + size + " type is " + type + " coffee with " + flavour + ".")
else:
    print("You asked for a " + size + " type is " + type + " coffee.")
    price3 = price2

priceNoTip = float(price3)
priceWithTip = float((price3 * 0.15) + priceNoTip)
finalPrice = "{:.2f}".format(priceWithTip)  
    
print("Your cup of coffee costs", priceNoTip)

print("The price with a tip is", finalPrice)
   
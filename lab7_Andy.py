# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Andy Phung
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Taco and Soda
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class item: Taco
    def __init__(self, name, price):
        self.name = name
        self.price = price

class item: Soda
    def __init__(self, name, price):
        self.name = name
        self.price = price

# TICKET @: Make your real items
#   Make 2 or 3 real items with you own names and prices. 
#   Predict what print(item1.name) shows, then run it

item1 = Taco("Steak Taco", 3)

item2 = Soda("Coke", 2)

Item3 = Soda("Sprite", 2)

# I think that if I were to run "print(item1.name)" it'll run "Steak Taco".


# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT: I think that it would say "I need money" because I added that line of code that should block anything under 0.
#   Paste the message you see here: 


item1.set_price(3)

item2.set_price(2)

item3.set_price(2)

item1.set_price(-5)

if price  < 0:
    print("I need money!!")


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class Shrimp_Taco(Taco):
    def __init__(self, name, price):
        self.name = Shrimp_Taco
        self.price = 3



# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: Because the two classes have the same instructions but have different trigger statements.


class Taco:
    def deliver(self):
        print("Delivering Taco's to your location!")

class Soda: 
    def deliver(self):
        print("Delivering Soda's to your location!")

Taco = Taco

Soda = Soda

Taco.deliver()
Soda.deliver()


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def__init__(self):
        self.items = []
    def add(self, item): 
        self.items.append(item)


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.

my_caart.checkout()


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

store = {"1": item1, "2": item2, "3" item3}

cart = cart()


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______________

while True:
    print("\nAvailable items:")
    for key, value in store.items():
        print(f"{key}: {value}")

    choice = input("Enter the item number youw want to add, or type "done": ")

    if choice.lower() == "done":
        break
    elif choice in store: 
        cart.append(store[choice])
        print(f"Added {store[choice]} to you ccart!")
    else:
        print("Invalid choice, please try again")

print("Your cart:", cart)


# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================

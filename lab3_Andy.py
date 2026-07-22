#Andy Phung | Lab 3 | Hustle program

#Ticket 1

username = ("lunavzzc")

print(len(username))

#Predict = My handle is 8 characters long
#Explain = Yes, the len() did count every character

#Ticket 2 

print(username[0])

print(username[len(username) - 1])

#Predict = The two letters that will print are l and c
#Explain = Python starts counting string indexes at 0, and the final character is one position before the total number of characters

#Ticket 3

print("Welcome to Loop, @" +username+ "!")

print(f"Welcome to Loop, @{username}!")

#Predict = Yes, I think both lines will be identical on screen because both lines of codes are meant to have the same output
#Explain = I think that the f string method felt easier because I had to do less things


#Ticket 4

username[0] = "X"

#  username[0] = "X"

print(username.upper())

#Predict = I think when I run the broken line an error will pop up
#Explain = Immutable means a string can't be changed after its created


#Ticket 5

feed = [
    "Good morning friends"
    "Im really hungry"
    "I need to poop"
]

print(len(feed))
print(feed[0])

#Predict = The count printed will be 3 because there are three captions in the list. The caption that'll print first is "Good morning friends"
#Explain = I used index 0 because python starts counting at 0, so the first item is always at index 0


#Ticket 6

feed.append("I want food")

#Predict = This post will be index 3, the order is index 0 to 1 to 2 then to 3.
#Explain = This post sits at index three because python starts its count at 0

#Ticket 7

feed.pop(0)
feed.sort()

#Predict = the first post is removed and now the other posts are in alphabetical order
#Explain = feed.sort() makes the posts go into alphabetical order


#Ticket 8

profile = {
    "username": "lunavzzc",
    "followers": 180,
    "verified": False
}

print(profile["followers"])

profile[0]

#Predict = The follwer number that prints will be 180. I think profile[0] will make an error
#Explain = The dictionary uses names instead of numbers to find information 

#Ticket 9

profile["followers"] = profile["follwers"] + 50

profile["bio"] = "Loves to eat"

print(profile)

print(profile.get("age"))

#Predict = the print(profile.get("age")) line won't do anything because "age" is not in the dictionary
#Explain = .get() is sager because it does not crash if the key is missing
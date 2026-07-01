#Andy Phung | Lab 5 | Intro to Python

#Ticket 1

ages = [17, 11, 25, 13, 9]
for age in ages:
    if age >=13:
        print("Access granted")
    if age <13:
        print("Too young")

Predict - The ages that will get "Access granted" will be 17, 25, and 13. Ages 11 and 9 will get "Too young"
Explain - The variable age holds numbers


    #Ticket 2

    keep_checking == "yes:"

    while keep_checking == "yes":
        age = int(input("Enter an age: "))
        if age >=13:
            print(f"{age} - Access granted")
        if age <13:
            print(f"{age} - Too young")

        keep_checking = input("Check another age? (y/n): ") 
        
Predict - If the user types no, the loop will just stop
Explain - A while loop is doing 2 things at once, checking the user's input and dishing out an output
   



   #Ticket 3
    while True: 
        user_input = input(type "Stop" to stop: )
        if user_input == "Stop":
            break
Predict - I think that if I forgot the break statement the loop would never end
Explain - The difference between ticket 2's while loop and this one's is how it checks the user input and how they end the loop

        




#Ticket 4 

def can_access(age): 
    if age >=13:
        return True
    if age <13:
        return False

ages = [17, 11, 25, 13, 9]
for age in ages:
    if can_access(age):
        print(f"{age} - Access granted")
    if cannot_access:
        print(f"{age} - Too young")

Predict - Not sure
Explain - it prevents code duplication


#Ticket 5

def signup_report(age_list):
    approved = 0
    print("--- StreamPass Signup Report ---")
    for number, age in enumerate(age_list, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} - Access granted")
            approved += 1
        else: 
            print(f"Signup #{number} | Age {age} - Too young")
        print(f"Approved: {approved} out of {len(age_list)}")
    
    signups = [22, 10, 15, 8, 19, 13]
    signup_report(signups)

 Predict - Signup #1 | Age 22 - Access granted
           Signup #2 | Age 10 - Too young
           Signup #3 | Age 15 - Access granted
           Signup #4 | Age 8 - Too young
           Sighup #5 | Age 19 - Access granted
           Signup #6 | Age 13 - Access granted
           Approved: 4 out of 6
Explain - Functions, Loops, Conditions
"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. 
Your code should look something like this:
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
• Look closely at your results, and make sure you understand why each line evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

"""

players = ["Lebron James", "Luka Doncic", "Austin Reaves", "Jared Vando", "Mark Williams", "Gabe Vincent", "Jaxson Hayes", ]

if 'Anthony Davis' not in players:
    print("you have been traded\n")
else: 
    print("glad you're still on our team\n")

if 'Lebron James' in players:
    print("you survived the trade deadline\n")
else: 
    print("we will miss you\n")


jerseyNumber = 24

if jerseyNumber <= 8: 
    print("this is your jersey number\n")
else: 
    print("this isn't your jersey number\n")


if jerseyNumber >= 21:
    print("you can have this jersey number\n")
else: 
    print("you cannot have this jersey number\n")

if jerseyNumber == 24 or jerseyNumber == 8:
    print("these number belong to Kobe! denied\n")
else: 
    print("you can wear this number\n")

if jerseyNumber > 24 or jerseyNumber < 8:
    print("this jersey can be worn\n")
else: 
    print("this jersey cannot be worn\n")

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

"""

alien_color = "green"

if alien_color == "green":
    print("you have earned 5 points\n")
if alien_color == "red":
    print("")


"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""




alien_color2 = "orange"
if alien_color == "green":
    print("you have earned 5 points\n")
else: 
    print("you have earned 10 points\n")

if alien_color2 == "orange":
    print("you gained 5 points\n")
else: 
    print("you gained 10 points\n")

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif- else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.

"""

alien_color3 = "yellow"

if alien_color3 == "green":
    points = 5
elif alien_color3 == "green":
    points = 5
elif alien_color3 == "yellow":
    points = 15

print(f"you earned {points} points!\n")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.

"""

age = 34

if age < 2:
    print("this person is a baby\n")
elif age >= 2 and age < 4: 
    print("this person is a toddler.\n")
elif age >= 4 and age < 13:
    print("this person is a kid.\n")
elif age >= 13 and age < 20:
    print("this person is a teenager.\n")
elif age >= 20 and age < 65:
    print("this person is an adult.\n") 
else:
    print("this person is an elder\n")

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
    If the fruit is in your list, the if block should print a statement, such as You really like bananas!

"""

favFruits = ["mangos", "bananas", "grapes", "apples"]

if "bananas" in favFruits: 
    print("you really like bananas\n")
if "mangos" in favFruits:
    print("you really like mangos\n")
if "grapes" in favFruits:
    print("you really like grapes\n")
if "apples" in favFruits:
    print("you really like apples\n")
if "kewi" in favFruits:
    print("you really like kewi\n")

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

"""

userNames = ["MichaelScott", "JimHalpert", "OscarMartinez", "PamBeasley","KevinMalone,", "admin"]
for user in userNames:
    if user == 'admin':
        print(f"Hello admin, would you like to see status reports?")
    else: 
        print(f"greetings {user}! thank you for logging on!\n")

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct mes-
sage is printed.

"""

userNames = []
if userNames:
    for user in userNames:
        print(f"Welcome {user}!\n")
else: 
    print("We need to find some users!\n")

"""
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

"""

current_users = ["userName0", "userName1","userName2","userName3","userName4"]
new_users = ["userName0","userName5","userName6","userName7","userName8"]
for user in new_users:
    if user in current_users:
        print(f"{user} is already in use\n")
    else: 
        print(f"{user} available\n")

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

"""

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers: 
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif number in range(4,10):
        print(f"{number}th")
    
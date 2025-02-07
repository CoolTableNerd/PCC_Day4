# PCC Day 4

Chapter 5 covers if-statements
• deciding on actions to take based on conditions 


### Chapter 5 Notes

if-statements is an expression can be evaluated as True or False –– called conditional 

checking for equality ––  determine if two values are equal two equal signs 'equality operator' (==) evaluate if the variable matches the value
- equality operator is case sensitive -– "Pants" is not the same as "pants"
    - methods can be attached to control entry if case sensitivity (not recommended for passwords) `pants.lower()` | `pants.upper()`

sneaker = "vomeros" <- value assigned to a variable
sneaker == "vomeros" –– result: True 

`if sneaker == "vomeros":` ––> if starts the condition for a variables value to be evaluated.

if statements –– conditional + action inside body

if value [condition]:
    [action] ––> action must be indented 

if value [condition]:
    [action] 
else: ––> semi-colon with the action indented underneath
    [different action]

checking for inequality –– determine if two values are NOT equal with inequality operator (!=)
coat = "North Face" 
coat == "Canada Goose" –– result: False

if coat != 'Canada Goose': 
    print("wearing my North Face)

numerical comparison: comparing two numbers

answer = 12 ––> an answer submitted by user
if answer != 24: ––> number in the condition does not need parenthesis or quotes 
    print("your answer is wrong)

age = 18

if age == 18:
    print("you are of age)

mathematical comparison can be included in conditional statements
age = 21

if age < 21: (less than sign)
    print (true)
else
    print (false)    

results: prints false. 21 is not less than 21. 

if age > 21: (greater than sign)
    print(true)
else
    print(false)

result: prints false. 21 is not greater than 21. 

if age <= 21: (less than or equal to)
    print(true)
else:
    print(false)

result: prints true. 18 is less than 21

if age >= 21: (greater than or equal to)
    print(true)
else: 
    print(false)

result: prints false. 18 is not greater than or equal to 21

Multiple conditions can be checked at the same time using keywords `and` or `or`
- the condition has to be included with both comparisons

`and` –– both conditions need to be true. "today is Thursday AND the 6th of February

age_0 = 8
age_1 = 24

if age_0 <= 7 or age_1 <= 10:
    print(false) ––> prints false because one statement is false


`or` –– only one of the conditions need to be true. "the grapes are green or purple"

age_0 = 8
age_1 = 24

if age_0 >= 21 or age_1 >= 21:
    print(true) ––> prints true because one statement is true. 

checking if a list contains a certain value using the `in` keyword (RWE: checking if a new username already exist)

userNames = ["CoolTableNerd","]

if 'CoolTableNerd' in userNames: 
    print("this userName is already in use")
else: 
    print("userName created")

results: 'this userName is already in use' will be printed.

checking if a list does not contain a certain value using the `not` keyword.

bannedList = ["Logan", "Jake", "Hugan"]

if 'Tyson' not in bannedList: 
    print("you can proceed")
else:
    print("you are banned)

Boolean values are used to keep track of certain conditions using `true `or `false`
game_active = True
can_edit = False 

if-elif-else: run each conditional test in order until one passes 
- Python does not require an else block at the end of an if-elif chain.
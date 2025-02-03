#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
'''
AND
|  A    |   B    |  A&B  |
--------------------------
|  True | False  | False |
|  False| True   | False |
|  True | True   | True  |
|  False| False  | False |

OR
|  A    |   B    | A OR B|
--------------------------
|  True | False  | True  |
|  False| True   | True  |
|  True | True   | True  |
|  False| False  | False |

Not B
|  A    |   B    | A OR B|
--------------------------
|  True | False  | True  |
|  False| True   | False |
|  True | True   | False |
|  False| False  | True  |

'''
#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
lightlevel = float(input("From 1 to 10 how dark is it outside?"))
if lightlevel < 8:
    headlights = True
    print ("Your headlights are on.")
else:
    headlights = False
    print ("Your headlights are off.")

#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
bankbalance = float(input("What is your bank balance? "))

if bankbalance > 100:
    print ("True")

else:
    print ("False")

#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
user_age = float(input("How old are you? "))
if user_age < 13:
    print ("You can only watch G rated Movies.")
elif user_age <= 17:
    print ("You can watch PG-13 or G rated Movies.")
else:
    print ("You can watch any of our Movies.")

#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
order = float(input("How much is your order? "))
if order < 50:
    print (f"Your total is: ${order+5:.2f}")
else:
    print (f"Your total is: ${order:.2f}")

'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
phrase = input("Write a phrase and I'll count the vowels. ")
def count_vowels(phrase):
    vowels = ("aeiouAEIOU")
    result=0
    for letter in phrase:
        if letter in vowels:
            result += 1
        else:
            continue
    print (result)
count_vowels(phrase)

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(yarn):
    yarn = yarn.lower()
    backward = ""
    for letter in yarn:
        backward += letter
    if yarn == backward:
        print(yarn, "is a palindrome.")
    else:
        print(yarn, "is not a palindrome.")

yarn = input("Type something and I'll tell you if it's a palindrome. ")
is_palindrome(yarn)

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "It's Super Effective!"
    elif attacker == "Fire" and defender == "Water":
        return "It's Not Very Effective..."
    elif attacker == "Electric" and defender == "Grass":
        return "It's Neutral."

attacker = input("What type of pokemon is attacking? ")
defender = input("What type of pokemon is defending? ")
print(type_advantage(attacker, defender)

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    if vehicle == "yes":
        vehicle = 10
    elif vehicle == "Yes":
        vehicle = 10
    elif vehicle == "YES":
        vehicle = 10
    else:
        vehicle = 0
    if age >= 65:
        vehicle += 5
    elif age >= 19:
        vehicle += 10
    else:
        vehicle = 0
    return vehicle
age = float(input("How old are you? "))
vehicle = input("Are you driving on? ")
print ("Your fare is: $", ferry_fare(age, vehicle))

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience, level):
    if experience <= 99:
        level = "Level 1"
    elif experience <= 199:
        level = "Level 2"
    else:
        level = "Level 3"
    return level
experience = int(input("How much experience have you gained? "))
level = 'Level 1'
print ("You are now", level_up(experience, level))

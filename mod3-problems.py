# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word= input("What is the word?")
word= word + " "
wordnum= int(input("How many times should I repeat it?"))
print (word*wordnum)
#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
yourname = input("What is your name? ")
age = int(input("How old are you? "))
age2 = age+1
print("Hello, " + yourname + "! You are " + str(age) + " years old. Next year, you will be " + str(age2) + " years old.")
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Write me a sentence: ")
werd = input("What word do you want me to check for in that sentence? ")
if werd in sentence:
    print(werd + " is in your sentence.")
else:
    print(werd + " is not in your sentence.")
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Give me a word. ")
dex1 = int(input("What is the first index? "))
dex2 = int(input("What is the last index? "))
print (word[dex1:dex2])
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print ("eye","love","python", sep="|")

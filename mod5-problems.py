#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Enter a positive number. "))
#ngl, this one took a second to wrap my head around even though I knew it was simple.
#intlist = list(range(1,n+1))
#total = sum(intlist)
#print (total)
i = 1
while i <= n:
    a = i+1
    b = a+i
   # print (i,a,b)
    i += 1
print (b)
#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.
shtring = "tubular"
for i in shtring:
    print (i.upper())
#3. Use a for loop and the range() function to print all even numbers from 2 to 20.
for i in range(2,21,2):
    if i==10:
        continue
    print (i)
#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:
# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25
#i'm confused on how to get the spacing right after the 3rd line because of 2 digits
for i in range(1,6):
    for a in range(1,6):
        print(a*i, sep=' ', end='  ')
    print ()
#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.
unum = 1
while unum != 0:
    unum = int(input("Enter a number, (enter 0 to stop)"))
    print ("You entered", unum)
print ("Exiting...")

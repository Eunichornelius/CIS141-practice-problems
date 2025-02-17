#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numlist = [1, 2, 3, 4, 5, 6, 14, 16, 18, 7, 9, 11, 20]
evennumbers = []
for element in numlist:
    if element % 2 == 0:
        #evennumbers += element
        #print (element)
        evennumbers.append(element)
#print (evennumbers)
print(sum(evennumbers))
#two ways to solve this one, but I think this is the one that you wanted to see.

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
wordlist = ["Olympic", "Cascade", "Bigfoot", "Olympics", "Olympic", "Mountain", "College", "High School", "olympic", "Olympic"]
thecount = 0
for elem in wordlist:
    if "Olympic" == elem:
       thecount+=1
print ("Olympic appears in this list ", thecount, "times.")

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
listless = ["on", "one", "oneness", "no", "none", "noneness", "It", "in", "Ni", "Ni!", "nine", "nein!"]
listyess = []
for word in listless:
    if len(word) > 3:
        listyess.append(word)
        #print (word)
print (listyess)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
numblist = [1, 2, 3, 4, 5, 6, 14, 16, 18, 7, 9, 11, 20, 33, 58, 29, 55, 32, 64, 128, 256, 512, 1028, 999]
evennumber = []
oddnumber = []
for elementary in numblist:
    if elementary % 2 == 0:
        evennumber.append(elementary)
    else:
        oddnumber.append(elementary)
print("There are ", len(evennumber), "even numbers and ", len(oddnumber), " odd numbers.")

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
numbrelist = [1, 2, 3, 4, 5, 6, 14, 16, 18, 7, 9, 11, 20, 33, 58, 29, 55, 32]
squarelist = []
for numbre in numbrelist:
   squarelist.append(numbre**2)
print(squarelist)

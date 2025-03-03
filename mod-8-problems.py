'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
'''
tips = open("gardening_tips.txt", "w")
tips.write("Don't use salt water to water your vegetable plants, it will not make your vegetables taste better.\n")
tips.write("Rabbits are cute, but wild rabbits will destroy your garden. Deer are also a nuisance.\n")
tips.write("Poisoning Rabbits and Deer is illegal. It will also not make them taste better.")
tips.close()
'''
with open("gardening_tips.txt", "r") as file:
    for line in file:
        print(line)

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
hname = 1
while hname != 0:
    hlog = open("hiking_log.txt", "a")
    hname = input("What is the name of your hike? (0 to exit)")
    if hname == "0":
        break
    hdistance = input("How many miles was your hike? ")
    hlog.write(hname + ' ' + str(hdistance) + "m \n")
hlog = open("hiking_log.txt", "r")
print (hlog.read())
hlog.close()
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
with open("songlyrics.txt", "r") as lyric:
    lyrics = lyric.read()
lyrics = lyrics.lower()
wordcount = 0
words = {}
while wordcount < 5:
    word = input("Give me a word that you want to check for in this song. ")
    word = word.lower()
    words[word] = lyrics.count(word)
    wordcount += 1
print (words)
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt", 'r') as poll:
    politics = poll.read()
yea_votes = politics.count("yea")
nay_votes = politics.count("nay")
print (yea_votes, "in favor, ", nay_votes, "opposed.")

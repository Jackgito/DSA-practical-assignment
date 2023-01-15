# BM40A1500 Data Structures and Algorithms practical assignment - Open hashing

# This program uses a list to store all the data
# It can read and save data from one text file,
# then it reads second text file and tries to find matching words from both of the files

import time

def main():
    wordList = []
    # Time is used to see how long each step of the program takes
    start_time = time.time()
    try:
        words_alpha = open("words_alpha.txt",  "r", encoding = "UTF-8")
        kaikkisanat = open("kaikkisanat.txt", "r", encoding = "UTF-8")
    except:
        print("File wasn't found")
        exit()

    print("Reading words from file 'words_alpha'")
    for i in words_alpha:
        wordList.append(i)

    words_alpha.close()

    print("Time to add the words: %.8s seconds\n" % (time.time() - start_time))

    matchingWords = 0
    print("Comparing words from 'kaikkisanat' to 'words_alpha'")
    for i in kaikkisanat:
        for j in wordList:
            if i == j:
                matchingWords += 1

    kaikkisanat.close()

    print("Time to find the common words: %.8s seconds\n" % (time.time() - start_time))

    print("words_alpha and kaikkisanat had " + str(matchingWords) + " matching words.")
    return

main()

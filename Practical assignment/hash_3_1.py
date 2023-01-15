# BM40A1500 Data Structures and Algorithms practical assignment - Open hashing

# This program uses linked lists to store the values in the hashtable
# It can read and save data from one text file,
# then it reads second text file and tries to find matching words from both of the files

import hash_1

import time

def main():
    # Time is used to see how long each step of the program takes
    start_time = time.time()
    hashTable = hash_1.HashTable(10000)
    print("Time to initialize the hash table: %.8s seconds\n" % (time.time() - start_time))
    start_time = time.time()
    try:
        words_alpha = open("words_alpha.txt",  "r", encoding = "UTF-8")
        kaikkisanat = open("kaikkisanat.txt", "r", encoding = "UTF-8")
    except:
        print("File wasn't found")
        exit()
    matchingWords = 0

    print("Reading words from file 'words_alpha'")
    for i in words_alpha:
        index = hashTable.hashing(i)
        hashTable.table[index].insert(i)

    words_alpha.close()

    print("Time to add the words: %.8s seconds\n" % (time.time() - start_time))
    start_time = time.time()

    print("Comparing words from 'kaikkisanat' to 'words_alpha'")
    for i in kaikkisanat:
        index = hashTable.hashing(i)
        if hashTable.table[index].search(i):
            matchingWords += 1

    kaikkisanat.close()

    print("Time to find the common words: %.8s seconds\n" % (time.time() - start_time))

    print("words_alpha and kaikkisanat had " + str(matchingWords) + " matching words.")
    hashDistribution = open("hashDistribution.txt", "w", encoding="UTF-8")
    counter = 0

    # Check the lenght of each linked list and save them to text file for hash analysis
    for i in hashTable.table:
        lenght = i.getLenght()
        hashDistribution.write(str(counter) + ";" + str(lenght) + "\n")
        counter += 1
    hashDistribution.close()
    return

main()

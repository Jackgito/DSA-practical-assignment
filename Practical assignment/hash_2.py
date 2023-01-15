# BM40A1500 Data Structures and Algorithms practical assignment - Open hashing

# This program uses linked lists to store the values in the hashtable
# It can search, insert and delete integers or strings

import hash_1

def main():
    hashTable = hash_1.HashTable(3)

    print("The structure of the hash table")

    items = [12, 'hashtable', 1234, 4328989, 'BM40A1500', -12456, 'aaaabbbbcccc']

    for i in items:
        hashTable.insert(i)
        hashTable.print()
        print()

    print("Find and print values -12456, 'hashtable' and 1235.")
    itemsToSearch = [-12456, 'hashtable', 1235]
    for i in itemsToSearch:
        index = hashTable.hashing(i)
        if hashTable.table[index].search(i):
            print(str(i) + " was found.")
        else:
            print(str(i) + " wasn't found.")

    print()
    print("Remove values 'BM40A1500', 1234, 'aaaabbbbcccc'.")
    itemsToDelete = ['BM40A1500', 1234, 'aaaabbbbcccc']
    for i in itemsToDelete:
        index = hashTable.hashing(i)
        if hashTable.table[index].delete(i):
            print(str(i) + " was deleted.")
        else:
            print(str(i) + " wasn't found.")

    print("\nThe structure of the hash table")
    hashTable.print()

main()
# BM40A1500 Data Structures and Algorithms practical assignment - Open hashing

# This program uses linked lists to store the values in the hashtable
# It can search, insert and delete integers or strings

import random

# Hash table
class HashTable:
    def __init__(self, size):
        self.size = size
        # Create linked lists for each slot in the hashtable
        self.table = [LinkedList() for i in range(size)]

    # The hash function uses random library to generate the hash code
    # based on if the first character of the inserted data is a vowel or not

    # If it is a vowel, seed used for the randomization is calculated from the
    #  sum of the ASCII values of the inserted data, minus its lenght

    # Otherwise it goes further multiplying that seed with the ASCII value of one
    # character in the inserted data.
    # This character is calculated by dividing the seed with lenght of the inserted data
    # and taking the remainder
    def hashing(self, data):
        vowels = ('a','e','i','o','u','y','ä','ö','å''A','E','I','O','U','Y','Ä','Ö','Å')
        seed = 0
        data = str(data)
        for i in data:
                seed += ord(str(i)) - len(data)
        if data[0] in vowels:
            random.seed(seed)
        else:
            seed = seed * ord(str(data[seed % len(data)]))
            random.seed(seed)

        index = random.randrange(0, self.size)

        return index

    # Prints the structure of the hash table and contents of linked lists
    def print(self):
        for i in range(len(self.table)):
            print("Index: " + str(i) + " |" + str(self.table[i].print()) + "|")
        return

    # Searches the hash table for element based on the hash value
    # and returns it, if it's found
    def search(self, data):
        index = self.hashing(data)
        if index >= 0:
            if self.table[index].search(data):
                return data
            else:
                return None

    # Uses hashing method to save data to hash table
    def insert(self, data):
        index = self.hashing(data)
        if index >= 0:
            self.table[index].insert(data)
        else:
            print("Insertion failed.")
        return

    # If wanted element is found, remove it
    def delete(self, data):
        index = self.hashing(data)
        if index >= 0:
            if self.table[index].delete(data):
                print(str(data) + " was deleted.")
            else:
                print(str(data) + " wasn't found.")
        return

# Node of linked list which contains data and location of the next node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
  
# Linked List which contains nodes that store all the data
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            return ""

        iterator = self.head
        string = ""
        while iterator != None:
            string += str(iterator.data)
            if iterator.next != None:
                string += " -> "
            iterator = iterator.next

        return string

    # Add data to the end of the linked list
    def insert(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next

        iterator.next = Node(data, None)
        return

    # Go through the linked list and if wanted element is found,
    # replace it with the next linked element or set it to none if there is no next element
    def delete(self, dataToDelete):

        iterator = self.head
        while iterator != None:
            if dataToDelete == iterator.data and iterator.next != None:

                iterator.data = iterator.next.data
                return True

            elif dataToDelete == iterator.data:

                iterator.data = None
                return True

            iterator = iterator.next
        return False

    # Iterate through the linked list until element is found or the list ends
    def search(self, data):
        iterator = self.head
        while iterator != None:
            if iterator.data == data:
                return True
            iterator = iterator.next
        return False

    # Get lenght of the linked list
    # Used in hash distribution analysis
    def getLenght(self):
        length = 0
        iterator = self.head
        while iterator != None:
            length += 1
            iterator = iterator.next
        return length
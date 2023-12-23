import os
import random

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.linkedList.head is None:
            return None
        else:
            node = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next
            if self.linkedList.head is None:
                self.linkedList.tail = None
            return node.value

    def peek(self):
        if self.isEmpty():
            return "The Queue is empty."
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(root_node, node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.leftChild is None:
            root_node.leftChild = BSTNode(node_value)
        else:
            insertNode(root_node.leftChild, node_value)
    else:
        if root_node.rightChild is None:
            root_node.rightChild = BSTNode(node_value)
        else:
            insertNode(root_node.rightChild, node_value)
    return "The node has been successfully inserted."


def inOrderTraversal(root_node, tempList):
    if not root_node:
        return
    inOrderTraversal(root_node.leftChild, tempList)
    tempList.append(root_node.data)
    inOrderTraversal(root_node.rightChild, tempList)


def treeSort(tempList):
    newTree = BSTNode(None)
    sortedList = []
    for x in tempList:
        insertNode(newTree, x)
    inOrderTraversal(newTree, sortedList)
    print(sortedList)


unsortedList = []

while True:
    print("1. Add a numbers")
    print("2. Generate a random array")
    print("3. Sort the numbers")
    print("4. Save numbers to a file")
    print("5. Load numbers from a file")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            try:
                num = input("Enter a number (or 'q' to exit): ")
                if num == 'q':
                    break
                num = float(num)
                unsortedList.append(num)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    if choice == "2":
        while True:
            try:
                length = int(input("Enter the length of the array: "))
                if length <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid length! Please enter a positive integer.")

        minimum = float(input("Enter the minimum value: "))
        maximum = float(input("Enter the maximum value: "))

        unsortedList = [round(random.uniform(minimum, maximum), 1) for i in range(length)]
        print("Random array generated (floating-point numbers):", unsortedList)

    elif choice == "3":
        sortedList = sorted(unsortedList)
        print("Sorted numbers:", sortedList)

    elif choice == "4":
        file_name = input("Enter the file name to save (in .txt format): ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        while os.path.exists(file_name):
            print("File already exists:", file_name)
            overwrite_choice = input("Do you want to overwrite it? (y/n): ")
            if overwrite_choice.lower() == "y":
                break
            else:
                file_name = input("Enter a new file name (in .txt format): ")
                if not file_name.endswith(".txt"):
                    file_name += ".txt"
        try:
            with open(file_name, 'w') as file:
                for num in unsortedList:
                    file.write(str(num) + '\n')
            print("Numbers saved to", file_name)
        except IOError:
            print("Error saving the file!")

    elif choice == "5":
        file_name = input("Enter the file name to load (in .txt format): ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        if not os.path.exists(file_name):
            print("File does not exist:", file_name)
        else:
            try:
                with open(file_name, 'r') as file:
                    unsortedList = [float(line.strip()) for line in file]
                print("Numbers loaded from", file_name)
            except IOError:
                print("Error loading the file!")
    elif choice == "6":
        break
    else:
        print("Invalid choice! Please enter a valid option.")
# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None
  
# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None
    
    def add_front(self, name):
        new_Node = Node(name)
        new_Node.next = self.head
        self.head = new_Node

    def add_end(self, name):
        new_Node = Node(name)
        if not self.head:
            self.head = new_Node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Node

    def remove(self, name):
        if not self.head:
            print('\nThe list is currently empty.')
        elif self.head.name == name:
            self.head = self.head.next
        else:
            current = self.head
            while current and current.name != name:
                current = current.next
            if not current:
                print('\nCustomer is not in the waitlist.')
            else:
                current.name = current.next.name
                current.next = current.next.next
    
    def print_list(self):
        current = self.head
        if not current:
            print('The list is currently empty.')
        else:
            while current:
                print(current.name)
                current = current.next

def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("\nEnter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("\nEnter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("\nEnter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("\nCurrent waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

        elif choice == "5":
            print("\nExiting waitlist manager.")
            break

        else:
            print("\nInvalid option. Please choose 1-5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200-300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''

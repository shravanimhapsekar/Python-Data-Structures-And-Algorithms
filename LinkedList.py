class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self,index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


my_LL = LinkedList(1)
print("Head:", my_LL.head.value)      
print("Tail:", my_LL.tail.value)
print("Length:", my_LL.length)

# append method
my_LL.append(2)
my_LL.append(3)
my_LL.append(4) 
my_LL.append(5) 
my_LL.print_list()

# prepend and pop method
print(f"Popped Element: {my_LL.pop().value}")
print("Prepend element is 1.")
my_LL.prepend(0)
my_LL.print_list()

# pop first method
print("First element has been popped!")
my_LL.pop_first().value
my_LL.print_list()

# get value method
while True:
    index = int(input("Enter the index no. to fetch value from: "))
    if index < 0 or index >= my_LL.length:
        print("Not a valid index. Please try again.")  
    else:
        node = my_LL.get_value(index)
        print(f"Value at index {index} is {node.value}")
        break  

# set value method
while True:
    index = int(input("Enter the index no. at which you want to set value: "))
    if index < 0 or index >= my_LL.length:
        print("Invalid index. Cannot set value.")
    else:
        value = int(input("Enter the value you want to set: "))
        my_LL.set_value(index, value)
        print(f"Value at index {index} updated to {value}")
        my_LL.print_list()
        break

# insert value method
while True:
    index = int(input("Enter the index no. at which you want to insert value: "))    
    if index < 0 or index > my_LL.length:
        print("Not a valid index. Please try again.")
    else:
        value = int(input("Enter the value you want to insert: "))
        my_LL.insert(index, value)
        print(f"Value {value} inserted at index {index}")
        my_LL.print_list()
        break

# remove method
while True:
    index = int(input("Enter the index of the node to remove: "))
    
    if index < 0 or index >= my_LL.length:
        print("Not a valid index. Please try again.")
    else:
        removed_node = my_LL.remove(index)
        print(f"Node with value {removed_node.value} removed from index {index}\n")
        my_LL.print_list()
        break

# reverse method
print("Reversed List:")
my_LL.reverse()
my_LL.print_list()


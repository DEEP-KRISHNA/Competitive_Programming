"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        # pass
        new_element.next = self.head
        self.head = new_element
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        # pass
        if (not (self.head)):
            return None
        temp = self.head
        self.head = temp.next
        # temp = None
        return temp.value
    
    def display(self):
        current = self.head
        print(current.value)
        if self.head:
            while current.next:
                print(current.value)
                current = current.next
        else:
            print(None)

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        # pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        # pass

    def display(self):
        self.ll.display()

if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    stack = stack(e1)
    # stack.display()
    stack.push(e2)
    stack.push(e3)
    stack.display()
    print(stack.pop())
    stack.pop()
    stack.push(e4)
    

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # new_element.next = self.head
        # self.head = new_element
        ele = self.head
        while (ele.next != None):
            ele = ele.next
        ele.next = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        pos = 1
        ele = self.head
        while (ele != None):
            if (pos == position):
                return ele
            pos += 1
            ele = ele.next
        return None
        # pass
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        # if (position == 1):
        #    append(self, new_element)
        # else:
        if(True):
            pos = 1
            ele = self.head
            while (ele != None):
                if (pos == position-1):
                    temp = ele.next
                    ele.next = new_element
                    ele.next.next = temp
                    break
                    # return ele.value
                pos += 1
                ele = ele.next
        # pass
        
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        # pass
        dell = self.head
        temp = self.head.next
        self.head = temp
        dell = None
    
    def display(self):
        ele = self.head
        while (ele != None):
            print(ele.value)
            ele = ele.next

if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    # ll.display()
    print(ll.get_position(3).value)
    print(ll.get_position(2).value)
    e4 = Element(4)
    ll.insert(e4, 3)
    print(ll.get_position(3).value)
    ll.delete(1)
    ll.display()

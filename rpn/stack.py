class Stack:                                # standard stack datatype;
    def __init__(self, element=None):
        self.storage = list()

    def push(self, element):                # element(int / str) -- element you want to add into the Stack;
        # --> function returns name of the added elment;
        self.storage.append(element)
        return element

    def pop(self):                          # --> function pops the last element you put into the Stack and returns its name;
        temp = self.storage[-1]
        self.storage.pop(-1)
        return temp

    def peek(self):                         # --> function returns the last value pushed to the Stack;
        try: return self.storage[-1]
        except IndexError: pass

    def length(self):                       # --> function returns number of elements in the Stack;
        return len(self.storage)

    def is_empty(self):                     # --> function returns True if Stack is empty, otherwise, returns False;
        return self.length() == 0

    def inside(self, element):              # element(int / str) -- name of element you want to check for;
        # --> function returs True if element is in the Stack, otherwise, returns False;
        return element in self.storage
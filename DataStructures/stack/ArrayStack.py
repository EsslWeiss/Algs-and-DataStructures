import sys
import ipdb
from Stack import Stack


class ArrayStack(Stack):
    # Default stack implementation

    def __init__(self):
        self.data = []
        self._stk_size = 0

    def size(self):
        return self._stk_size

    def is_empty(self):
        return self.size() == 0

    def push(self, elem):
        self.data.append(elem)
        self._stk_size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack was empty!")
        
        self._stk_size -= 1
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack was empty!")

        return self.data[self._stk_size - 1]
    
    def clear_stack(self):
        while self.is_empty() is False:
            self.pop()
         
    def pop_to(self, elem):
        while True:
            if elem == self.data[self._stk_size - 1]:
                return

            self.pop()


if __name__ == "__main__":
    arr_stk = ArrayStack()
    
    arr_stk.push(100.9)
    arr_stk.push(200.9)
    arr_stk.push(300.9)
    arr_stk.push(100.9)
    arr_stk.push("Name")
    arr_stk.push("Surname")
    arr_stk.push("#User position")

    print("Last element: %s" % arr_stk.peek())
    print("Current size: %s\n" % arr_stk.size())

    print("Poping %s" % arr_stk.pop())
    print("Poping %s\n" % arr_stk.pop())

    print("Last element: %s" % arr_stk.peek())
    print("Current size: %s\n" % arr_stk.size())

    arr_stk.pop_to(200.9)
    print("Stack after %s" % arr_stk.data)

    print("Final size: %s\n" % arr_stk.size())
    
    arr_stk.clear_stack()
    print("Size after clear: %s" % arr_stk.size())
    print("Stack after clear: %s\n" % arr_stk.data)


from abc import ABC, abstractmethod

class Stack:

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass
    
    @abstractmethod
    def clear_stk(self):
        pass


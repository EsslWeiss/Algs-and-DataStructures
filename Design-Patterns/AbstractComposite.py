from abc import ABC, abstractmethod


class Component(ABC):
   
    @abstractmethod
    def operation(self): pass

    def is_composite(self):
        return False

    def add(self, component): pass

    def remove(self, component): pass
    

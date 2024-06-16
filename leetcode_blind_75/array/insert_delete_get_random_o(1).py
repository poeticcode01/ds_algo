import random
class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.elements = []
        

    def insert(self, val: int) -> bool:
        element = val
        if element not in self.data:
            self.data[element] = len(self.elements)
            self.elements.append(element)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        element = val
        if element in self.data:
            index = self.data[element]
            last_element = self.elements[-1]
            self.elements[index] = last_element
            self.data[last_element] = index
            self.elements.pop()
            del self.data[element]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.elements)
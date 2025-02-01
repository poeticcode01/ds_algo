class Node:
    def __init__(self,key = None,val= None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.map = dict()
        

    def get(self, key: int) -> int:
        if self.map.get(key) is None:
            return -1

        temp_node = self.map[key]
        if self.head == temp_node:
            return temp_node.val
        else:
            prv = temp_node.prev
            nxt = temp_node.next
            if prv:
                if self.tail == temp_node:
                    self.update_tail(prv)
                else:
                    prv.next = nxt         
            if nxt:
                nxt.prev = prv
            
            temp_node.prev = None
            self.update_head(temp_node)     
        
        return temp_node.val

    def update_tail(self,prv):
        prv.next = None
        self.tail = prv
    

    def update_head(self,new_node):
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
            
        

    def put(self, key: int, value: int) -> None:
        if self.map.get(key) is None:
            new_node = Node(key,value)
            if self.size == self.capacity:
                if self.capacity == 1:
                    del self.map[self.head.key]    
                    self.head = new_node
                    self.tail = new_node   
                else:
                    del self.map[self.tail.key]
                    prv = self.tail.prev
                    self.update_tail(prv)
                    self.update_head(new_node)
            else:
                self.size +=1
                if self.head:
                    self.update_head(new_node)     
                else:
                    self.head = new_node
                    self.tail = new_node
        else:   
            temp_node = self.map[key]
            temp_node.val = value
            if self.head == temp_node:
                temp_node.val = value
            elif self.tail == temp_node:
                prv = temp_node.prev
                nxt = temp_node.next
                if prv:
                    self.update_tail(prv)
                if nxt:
                    nxt.prev = prv
                temp_node.prev = None
                self.update_head(temp_node)
            else:
                prv = temp_node.prev
                nxt = temp_node.next
                if prv:
                    prv.next = nxt
                if nxt:
                    nxt.prev = prv
                temp_node.prev = None
                self.update_head(temp_node)

        self.map[key] = self.head
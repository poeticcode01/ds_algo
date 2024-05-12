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
        # print(key,"tail",self.tail.key)
        temp_node = self.map[key]
        if self.head == temp_node:
            return temp_node.val
        elif self.tail == temp_node:
            prv = temp_node.prev
            nxt = temp_node.next
            if prv:
                prv.next = None
                self.tail = prv
                # print("prev",prv.key,prv.val)
                # print(key,"tail",self.tail.key)
            if nxt:
                nxt.prev = prv

            temp_node.prev = None
            temp_node.next  = self.head
            self.head.prev = temp_node
            temp_node.next = self.head
            self.head = temp_node
        else:
            prv = temp_node.prev
            nxt = temp_node.next
            if prv:
                prv.next = nxt
            if nxt:
                nxt.prev = prv
            
            temp_node.prev = None
            temp_node.next  = self.head
            self.head.prev = temp_node
            temp_node.next = self.head
            self.head = temp_node
        # self.map[key] = self.head
        return temp_node.val
            



        

    def put(self, key: int, value: int) -> None:
        # print(key,value,self.size)
        if self.map.get(key) is None:
            if self.size == self.capacity:
            
                if self.capacity == 1:
                    del self.map[self.head.key]
                    new_node = Node(key,value)
                    self.head = new_node
                    self.tail = new_node
                    
                else:
                    # print(key,value)
                    # print(self.tail.key,self.tail.val)
                    del self.map[self.tail.key]
                    temp = self.tail.prev
                    temp.next = None
                    self.tail = temp

                    new_node = Node(key,value)
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
            else:
                self.size +=1
                if self.head:
                    new_node = Node(key,value)
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                    # print(self.head.key,self.head.val)
                else:
                    new_node = Node(key,value)
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
                    prv.next = nxt
                    self.tail = prv
                if nxt:
                    nxt.prev = prv
                temp_node.prev = None
                temp_node.next  = self.head
                self.head.prev = temp_node
                temp_node.next = self.head
                self.head = temp_node
            else:
                prv = temp_node.prev
                nxt = temp_node.next
                if prv:
                    prv.next = nxt
                if nxt:
                    nxt.prev = prv
                temp_node.prev = None
                temp_node.next  = self.head
                self.head.prev = temp_node
                temp_node.next = self.head
                self.head = temp_node
        self.map[key] = self.head

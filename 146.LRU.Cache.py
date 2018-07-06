    
class ListNode:
    def __init__(self, v, b=None, n=None):
        self.value = v
        self.next = n
        self.before = b

class LRUCache:


        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        print("init start")
        import time
        t = time.time()
        self.hash = [-1] * (256 * 256 * 8)
        self.hash_list = [None] * (256 * 256 * 8)
        print(time.time() - t)
        self.counter = capacity
        self.head = None
        self.tail = None

    def trans(self, dig):
        return dig % (256 * 256 * 8)
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        key = self.trans(key)
        if self.hash[key] < 0:
            
            #self.check_list()
            return -1
        else:
            self.lift(self.hash_list[key])
            #self.check_list()
            return self.hash[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        key = self.trans(key)
        if self.hash[key] > 0:
            self.hash[key] = value
            self.lift(self.hash_list[key])
        elif self.counter == 0:
            self.remove()
            self.add(key, value)
        else:
            self.counter -= 1
            self.add(key, value)
        #self.check_list()
            
    def check_list(self):
        p = self.head
        while p:
            print(p.value, end="->")
            p = p.next
        print("\n")
        p = self.tail
        while p:
            print(p.value, end="->")
            p = p.before
        print("\n")
            
    def lift(self, node):
        #print('lift before', node.value, self.head.value, self.tail.value)
        #self.check_list()
        if node.before:
            node.before.next = node.next
            if not node.next:
                self.tail = node.before
                #print("re-tail", self.tail.value)
            else:
                node.next.before = node.before
            self.head.before = node
            node.next = self.head
            node.before = None
            self.head = node
        #print('lift after', node.value, self.head.value, self.tail.value)
        #self.check_list()
    
    def add(self, key, value):
        self.hash[key] = value
        p = ListNode(key, None, self.head)
        if not self.tail or not self.head:
            self.tail = p
            self.head = p
        else:
            self.head.before = p
        self.head = p
        self.hash_list[key] = self.head
        
        
    def remove(self):
        self.hash[self.tail.value] = -1
        self.hash_list[self.tail.value] = None
        if not self.tail.before:
            self.head = self.tail = None
        else:
            self.tail = self.tail.before
            self.tail.next = None
                       
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
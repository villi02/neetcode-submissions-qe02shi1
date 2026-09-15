class DLNode:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tab = {}
        self.tail = DLNode(0, 0)
        self.head = DLNode(0, 0)
        self.tail.next = self.head
        self.head.prev = self.tail
    
    def move_to_front(self, node):
        if node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node

    def delete_entry(self):
        lru = self.tail.next          # real LRU, not the dummy
        lru.prev.next = lru.next
        lru.next.prev = lru.prev
        del self.tab[lru.key]

    def get(self, key: int) -> int:
        if key not in self.tab:
            return -1
        else:
            self.move_to_front(self.tab[key])
            return self.tab[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.tab:
            self.move_to_front(self.tab[key])
            self.tab[key].val = value
        else:
            self.tab[key] = DLNode(value, key, next=None, prev=None)
            self.move_to_front(self.tab[key])
            if len(self.tab) > self.capacity:
                self.delete_entry()
        
        

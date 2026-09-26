class Node:
    def __init__(self, val, key, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = dict()
        self.dummy_end = Node(0, 0)
        self.dummy_head = Node(0, 0)
        self.dummy_head.next = self.dummy_end
        self.dummy_end.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.move_to_front(key).val
            
        else:
            return -1

    def move_to_front(self, key) -> None: 
            #assuming key is in self.cache
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.dummy_head.next
            self.dummy_head.next.prev = node
            self.dummy_head.next = node
            node.prev = self.dummy_head
            return node
        
    def put(self, key: int, value: int) -> Node:
        if key in self.cache:
            self.move_to_front(key)
            self.cache[key].val = value

        else:
            # for this block I am assuming size >= 1
            if self.size == self.capacity:
                lru = self.dummy_end.prev
                self.dummy_end.prev.prev.next = lru.next
                lru.next.prev = lru.prev
                lru.next = None
                lru.prev = None
                del self.cache[lru.key]

            else:
                self.size += 1

            new_node = Node(value, key)
            self.cache[key] = new_node
            new_node.next = self.dummy_head.next
            self.dummy_head.next.prev = new_node
            new_node.prev = self.dummy_head
            self.dummy_head.next = new_node

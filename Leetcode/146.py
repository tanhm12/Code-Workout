class  Node:
    def __init__(self, key: int = 0, val: int = 0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
    def __repr__(self):
        return f"[[key: {self.key}, prev: {self.prev.key if self.prev else None}, next: {self.next.key if self.next  else None}]]"

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.objs = {}
        self.head = Node(-1)
        self.tail = Node(-2)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int):
        if key not in self.objs:
            return -1
        else:
            node: Node = self.objs[key]
            self.move_node(node)
            return node.val
        

    def put(self, key: int, value: int):
        if key in self.objs:
            self.objs[key].val = value
            self.move_node(self.objs[key])
            return 
        
        if len(self.objs) == self.capacity:
            last_node: Node = self.tail.prev
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev
            del self.objs[last_node.key]
        
        # new_node = Node(key, value, self.head, self.head.next)
        new_node = Node(key, value, self.head, self.head.next)
        self.move_node(new_node, True)
        self.objs[key] = new_node
        
            
    def move_node(self, node: Node, is_new=False):
        if not is_new:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
        
        node.next.prev = node
        node.prev.next = node
    
        


queries = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

# queries = ["LRUCache","put","put","put","put","get","get"]
# params = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

obj = LRUCache(params[0][0])
for i in range(1, len(queries)):
    if queries[i] == 'put':
        obj.put(params[i][0], params[i][1])
    else:
        print(obj.get(params[i][0]))
    
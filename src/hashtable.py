# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.resized = False
        self.resizing = False


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        djb2_hash = 5381
        for char in key:
            djb2_hash = djb2_hash * 33 + ord(char)
        return djb2_hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity
        # return hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash_index = self._hash_mod(key)
        if self.storage[hash_index] is None:
            self.storage[hash_index] = LinkedPair(key, value)
            self.count += 1
            self.resize()
        else:
            current = self.storage[hash_index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return current.value
                elif current.next is None:
                    current.next = LinkedPair(key, value)
                    self.count += 1
                    self.resize()
                    return current.next.value
                else:
                    current = current.next



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_index = self._hash_mod(key)
        current = self.storage[hash_index]
        prev_node = None
        while current is not None:
            if current.key == key:
                if prev_node is not None:
                    prev_node.next = current.next
                else:
                    self.storage[hash_index] = current.next
                self.count -= 1
                self.resize()
                return None
            elif current.next is not None:
                prev_node = current
                current = current.next
            else:
                print('SOMETHING IS WRONG')
        return None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_index = self._hash_mod(key)
        if self.storage[hash_index] is not None:
            current = self.storage[hash_index]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
            return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        load_factor = self.count / self.capacity
        print(load_factor)
        new_cap = self.capacity
        if load_factor > 0.7 and self.resizing is False:
            new_cap = self.capacity * 2
            self.resized = True
        elif load_factor < 0.2 and self.resized is True and self.resizing is False:
            new_cap = self.capacity / 2
        else:
            return
        self.capacity = int(new_cap)
        new_storage = [None] * self.capacity
        index = 0
        self.count = 0
        self.resizing = True
        for n in self.storage:
            if n is not None:
                cur = n
                while cur is not None:
                    new_storage[index] = cur
                    cur = cur.next
                    index += 1
        self.storage = [None] * self.capacity
        for n in new_storage:
            if n is not None:
                self.insert(n.key, n.value)
        print(self.capacity)
        self.resizing = False
        
        

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")

# ht1 = HashTable(9)
# ht1.insert('bob', 1)
# print(ht1.storage)
# ht1.insert('fred', 2)
# print(ht1.storage)
# ht1.insert('sally', 3)
# print(ht1.storage)
# ht1.insert('ashley', 4)
# print(ht1.storage)
# ht1.insert('sam', 5)
# print(ht1.storage)
# ht1.insert('jed', 6)
# print(ht1.storage)
# ht1.insert('tom', 7)
# print(ht1.storage)
# ht1.remove('bob')
# print(ht1.storage)
# print(ht1.retrieve('fred'))
# print(ht1.storage)
# print(ht1.retrieve('fred'))
# for l in ht1.storage:
#     if l is not None:
#         print(l)
#         print(l.next)

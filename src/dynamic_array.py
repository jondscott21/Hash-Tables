class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity # how much is currently allocated
        self.count = 0 # Count is how much is currently used
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            self.resize()
            return
        # Shift everything to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        
        # Insert our value
        self.storage[index] = value
        self.count += 1
    
    def append(self. value):
        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value)
        self.insert(0, value)

    def slice(self, beginning_index, end_index):
        # Beginning and end
        # subarray
        subarray = []
        
        for i in range(beginning_index, end_index):
            subar


        # return subarray

        

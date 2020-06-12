class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity

    class RingBufferFull:
        def append(self, item):
            self.storage[self.curr] = item
            self.curr = (self.curr + 1) % self.capacity
        def get(self):
            return self.storage

    def append(self, item):
        self.storage.append(item)
        if len(self.storage) == self.capacity:
            self.curr = 0
            self.__class__ = self.RingBufferFull

    def get(self):
        return self.storage
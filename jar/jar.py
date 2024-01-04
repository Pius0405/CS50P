class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceeded maximum amount")
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, val):
        if val < 0:
            raise ValueError("Wrong capacity")
        else:
            self._capacity = val

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val



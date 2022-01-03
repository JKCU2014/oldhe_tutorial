import threading


class ThreadSafeCircularQueue:

    def __init__(self, capacity: int):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def __len__(self):
        return self.count

    def add(self, message: str):
        with self.not_full:
            while self.is_full():
                self.not_full.wait()
            self.queue[self.tail] = message
            self.tail = (self.tail + 1) % len(self.queue)
            self.count += 1
            self.not_empty.notify_all()

    def remove(self):
        with self.not_empty:
            while self.is_empty():
                self.not_empty.wait()
            message = self.queue[self.head]
            self.head = (self.head + 1) % len(self.queue)
            self.count -= 1
            self.not_full.notify_all()
            return message

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.queue)

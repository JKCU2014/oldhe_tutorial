import time
import threading


class DeadLockQueue:

    def __init__(self, initial_capacity: int):
        self.queue = [None] * initial_capacity
        self.head = 0
        self.tail = 0
        self.count = 0
        self.lock = threading.Lock()

    def __len__(self):
        return self.count

    def add(self, message: str):
        """ Add a message at the tail of this circular_queue.

        :param message: the message to add to this circular_queue
        """
        with self.lock:
            while self.is_full():
                time.sleep(0)
            self.queue[self.tail] = message
            self.tail = (self.tail + 1) % len(self.queue)
            self.count += 1

    def remove(self):
        """ Pop a message at the head of this circular_queue.

        :return: the message that is at the head of this circular_queue
        """
        with self.lock:
            while self.is_empty():
                time.sleep(0)
            message = self.queue[self.head]
            self.head = (self.head + 1) % len(self.queue)
            self.count -= 1
            return message

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.queue)

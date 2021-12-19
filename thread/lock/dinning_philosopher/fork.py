import threading


class Fork:

    def __init__(self, item_index: int):
        self.item_index = item_index
        self.lock = threading.Lock()

    def taken(self, philosopher_index):
        self.lock.acquire()
        print('Philosopher #{:d} is taking fork #{:d}.'.format(
            philosopher_index, self.item_index))

    def put(self, philosopher_index):
        print('Philosopher #{:d} is putting down fork #{:d}.'.format(
            philosopher_index, self.item_index))
        self.lock.release()

    def __str__(self):
        return 'Fork[item_index={:d}]'.format(self.item_index)

import time
from abc import ABC, abstractmethod
from threading import Lock

from .fork import Fork


class Philosopher(ABC):
    NUM_ROUNDs = 10

    def __init__(self, index: int):
        self.index = index
        self.eating_times = 0
        self.thinking_times = 0
        self.left_fork = None
        self.right_fork = None

    def set_left_fork(self, left_fork: Fork):
        self.left_fork = left_fork

    def set_right_fork(self, right_fork: Fork):
        self.right_fork = right_fork

    def __call__(self, *args, **kwargs):
        if self.left_fork is None or self.right_fork is None:
            raise RuntimeError(
                "Please set both left and right forks for a philosopher.")
        for _ in range(Philosopher.NUM_ROUNDs):
            self.eat()
            self.think()

    def __str__(self):
        return '{:s}[index={:d}, left_fork={:s}, right_fork={:s}]'.format(
            self.__class__.__name__,
            self.index, str(self.left_fork), str(self.right_fork))

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def think(self):
        pass


class DeadLockPhilosopher(Philosopher):

    def __init__(self, index: int):
        super().__init__(index)

    def eat(self):
        self.left_fork.taken(self.index)
        time.sleep(0.1)
        self.right_fork.taken(self.index)
        time.sleep(0.1)
        self.eating_times += 1
        print('Philosopher #{:d} is eating.({:d} totally)'.format(
            self.index, self.eating_times))
        time.sleep(0.1)

    def think(self):
        self.left_fork.put(self.index)
        self.right_fork.put(self.index)
        self.thinking_times += 1
        print('Philosopher #{:d} is thinking.({:d} totally)'.format(
            self.index, self.thinking_times))
        time.sleep(0.1)


class ServedPhilosopher(DeadLockPhilosopher):

    def __init__(self, index: int, waiter: Lock):
        super().__init__(index)
        self.waiter = waiter

    def __str__(self):
        return super().__str__() + '[waiter={:s}]'.format(str(self.waiter))

    def eat(self):
        with self.waiter:
            self.left_fork.taken(self.index)
            time.sleep(0.1)
            self.right_fork.taken(self.index)
            time.sleep(0.1)
        self.eating_times += 1
        print('Philosopher #{:d} is eating.({:d} totally)'.format(
            self.index, self.eating_times))
        time.sleep(0.1)

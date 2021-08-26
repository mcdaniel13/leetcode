from random import randint


class RandomizedSet:
    def __init__(self):
        self.dic = dict()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.arr.append(val)
            self.dic[val] = len(self.arr) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.dic:
            self.dic[self.arr[-1]] = self.dic[val]
            self.arr[-1], self.arr[self.dic[val]] = self.arr[self.dic[val]], self.arr[-1]
            self.arr.pop(-1)
            self.dic.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr) - 1)]
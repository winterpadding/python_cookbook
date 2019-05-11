import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # Heap is ordered smallest to largest.  Therefore, use -ve priority
        # We are putting a 3-tuple in to the heap
        # using this index ensures ordering of two items with same priority
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1  # This index only ever increases

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # Gets the last item in the tuple


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()

    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

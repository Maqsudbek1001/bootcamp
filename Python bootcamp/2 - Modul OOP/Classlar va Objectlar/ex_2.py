class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Bu bo'sh"

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

age = int(input("son: "))

queue_obj = Queue()
queue_obj.enqueue(age)

print("Queue dagi elementlar soni:", queue_obj.size())

from task1 import Queue
q = Queue()
print(q.isEmpty())
q.enQueue(1)
q.enQueue(7)
q.enQueue(5)
q.enQueue(2)
print(q.display())
q.deQueue()
q.deQueue()
print(q.display())
q.enQueue(9)
print(q.isEmpty())
print(q.display())
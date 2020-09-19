import threading
import time
import random
from queue import Queue
from threading import current_thread

queue = Queue(5)


class Producer(threading.Thread):

    def run(self):
        thread_name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print(f"生产者{thread_name}生产了元素{num}")
            t = random.randint(1, 3)
            time.sleep(t)
            print(f"生产者{thread_name}睡眠了{t}秒")


class Consumer(threading.Thread):

    def run(self):
        thread_name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print(f"消费者{thread_name}消费了元素{num}")
            t = random.randint(1, 5)
            time.sleep(t)
            print(f"消费者{thread_name}睡眠了{t}秒")


p1 = Producer(name='p1')
p1.start()
p2 = Producer(name='p2')
p2.start()
p3 = Producer(name='p3')
p3.start()
c1 = Consumer(name='c1')
c1.start()
c2 = Consumer(name='c2')
c2.start()

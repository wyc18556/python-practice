import threading
import time
from threading import current_thread


class MyThread(threading.Thread):
    def __init__(self, args1, args2):
        super().__init__()
        self.args1 = args1
        self.args2 = args2

    def run(self):
        print(f"{current_thread().getName()} start")
        print(f"run(args1={self.args1}, args2={self.args2})")
        time.sleep(1)
        print(f"{current_thread().getName()} end")


threads = []
for i in range(1, 6, 1):
    myThread = MyThread(i, i + 1)
    myThread.start()
    threads.append(myThread)

for i in range(len(threads)):
    # 依次等待子线程执行完毕
    threads[i].join()

print(f"main thread:{current_thread().getName()} end")

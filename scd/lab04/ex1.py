import logging
import queue
from threading import Thread,Event
from queue import Queue
import time
import random

logging.basicConfig(level=logging.DEBUG,
format='[%(levelname)s] (%(threadName)s) %(message)s',)

class producer(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue=queue

    def run(self):
        for i in range(10):
            item=random.randint(0,256)
            self.queue.put(item)
            logging.debug("[producer] added=%d" % item)
            time.sleep(1)

class consumer(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue=queue
    
    def run(self):
        while True:
            item=self.queue.get()
            logging.debug("[consumer] get=%d" % item)
            self.queue.task_done()

if __name__ == '__main__':
    queue=Queue()
    t1=producer(queue)
    t2=producer(queue)
    t3=producer(queue)
    t4=producer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

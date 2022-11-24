from cmath import log
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
format='[%(levelname)s] (%(threadName)s) %(message)s')

def worker():
    logging.debug('worker running')
    return


w1= threading.Timer(3, worker)
w1.setName('worker1')
w2= threading.Timer(3, worker)
w2.setName('worker2')

logging.debug('Start')
w1.start()
w2.start()

logging.debug('waiting before canceling %s', w2.getName())
time.sleep(2)
logging.debug('canceling %s', w2.getName())
w2.cancel()
logging.debug('End')

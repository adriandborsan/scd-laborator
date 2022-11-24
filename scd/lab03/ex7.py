import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)s) %(message)s')

def worker1(e):

    logging.debug('asteapta evenimentul')
    eveniment=e.wait()
    logging.debug('Se continua procesarea ... ')

e = threading.Event()
w1= threading.Thread(name='worker1',target=worker1,args=(e,))
w1.start()

logging.debug('Evenimentul va fi generat ...')
time.sleep(3)
e.set()
logging.debug('Evenimentul a fost generat')

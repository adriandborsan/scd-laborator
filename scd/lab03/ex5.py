import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
format='[%(levelname)s] (%(threadName)s) %(message)s')

def daemon():
    logging.debug('Start...')
    time.sleep(5)
    logging.debug('End...')

d= threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


notD= threading.Thread(name='non-daemon', target=non_daemon)


d.start()
notD.start()
print('d is Alive=', d.is_alive())

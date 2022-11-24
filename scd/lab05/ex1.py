import multiprocessing
import time
import os

def afiseaza(id):
    print('procesul este ',id, ' | pid=',os.getpid())
    time.sleep(5)
    return
if __name__=='__main__':
    print('Start ... pid=',os.getpid())
    for i in range(5):
        p=multiprocessing.Process(target=afiseaza,args=(id,))
        p.start()
        p.join()
        
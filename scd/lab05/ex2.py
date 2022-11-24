import multiprocessing
import time
import os

def afiseaza(t):
    procName=multiprocessing.current_process().name
    print('Start process',procName,' | pid=',os.getpid())
    time.sleep(5)
    print('End process ',procName,' | pid=',os.getpid())

if __name__=='__main__':
    print('Start ... pid=',os.getpid())
    backgroundProc=multiprocessing.Process(name='background',target=afiseaza,args=(5,))
    backgroundProc.daemon=True

    foregroundProc=multiprocessing.Process(name='foreground',target=afiseaza,args=(5,))
    foregroundProc.daemon=False

    backgroundProc.start()
    foregroundProc.start()
    
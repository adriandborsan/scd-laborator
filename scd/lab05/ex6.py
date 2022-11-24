import multiprocessing

def trimiteDn(capat):
    capat.send(['abc', (1,2,3),11])
    capat.close()

if __name__=='__main__':
    capatA,capatB=multiprocessing.Pipe()
    p=multiprocessing.Process(target=trimiteDn,args=(capatA,))
    p.start()
    print(capatB.recv())
    p.join()
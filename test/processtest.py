import time
from multiprocessing import Process

def count(n):
    inp = n
    start = time.time()
    while n > 0:
        n -= 1
    else:
        stop = time.time()

if __name__ == '__main__':
    for n in range(100):
        p = Process(target=count,args=(1000,))
        p.start()
        print(p.name,p.pid)

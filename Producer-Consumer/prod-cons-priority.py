from threading import Thread
from threading import Lock
import time
import random
import Queue


lock = Lock()
# N == Buf_Size
Buf_Size = 8

q = Queue.Queue(Buf_Size)

class ProducerThread(Thread):
    def __init__(self,name,pri):
        super(ProducerThread, self).__init__()     
        self.name = name
        self.pri = pri

    def run(self):
        while True:
            if not q.full():
                # Generate the item
                item = random.randint(1,10)
                # lock.acquire()
                q.put(item)
                print 'Producing: ' + "Q size: " + str(q.qsize()) + ' itemVal:' +  str(item) 
                time.sleep(2*self.pri)
                # lock.release()
        return

class ConsumerThread(Thread):
    def __init__(self,name,pri):
        super(ConsumerThread, self).__init__()
        self.name = name
        self.pri = pri
 
    def run(self):
        while True:
            if not q.empty():
                # Generate the item
                # lock.acquire()
                item = q.get()
                print 'consuming: ' + 'Q size: ' + str(q.qsize()) + ' itemVal: ' + str(item) + ' Thread Name: ' + str(self.name) + ' pri: ' + str(self.pri) 
                time.sleep(2*self.pri)
                # lock.release()
        return

if __name__ == '__main__':
    p = ProducerThread(name = 'Producer', pri = 0.5)
    c1 = ConsumerThread(name = 'Consumer 1',pri = 0.75)
    c2 = ConsumerThread(name = 'Consumer 2', pri = 0.25)

    p.start()
    time.sleep(2)
    c1.start()
    c2.start()
    time.sleep(2)

    p.join()
    c1.join()
    c2.join()

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
    def __init__(self,name):
        super(ProducerThread, self).__init__()     
        self.name = name

    def run(self):
        while True:
            if not q.full():
                # Generate the item
                item = random.randint(1,10)
                # lock.acquire()
                q.put(item)
                print 'Producing: ' + "Q size: " + str(q.qsize()) + ' itemVal:' +  str(item) 
                time.sleep(random.random())
                # lock.release()
        return

class ConsumerThread(Thread):
    def __init__(self,name):
        super(ConsumerThread, self).__init__()
        self.name = name
 
    def run(self):
        while True:
            if not q.empty():
                # Generate the item
                # lock.acquire()
                item = q.get()
                print "Consuming: " + 'Q size: ' + str(q.qsize()) + ' itemVal: ' + str(item) + ' Thread Name: ' + str(self.name)  
                time.sleep(random.random())
                # lock.release()
        return

if __name__ == '__main__':
    p = ProducerThread(name = 'Producer')
    c1 = ConsumerThread(name = 'Consumer 1')
    c2 = ConsumerThread(name = 'Consumer 2')

    p.start()
    time.sleep(2)
    c1.start()
    c2.start()
    time.sleep(2)

    p.join()
    c1.join()
    c2.join()

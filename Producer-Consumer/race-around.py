from threading import Thread
from threading import Lock

lock = Lock()

# define a global variable
some_var = 0

class IncrementThread(Thread):
    def __init__(self):
        # self.name = name
        super(IncrementThread, self).__init__()

    def run(self):
        # we want to read a global variable 
        # and then increment it by 1

        global some_var
        lock.acquire()
        read_value = some_var
        print "Some_var in %s is %d" % (self.name, read_value)
        
        some_var = read_value + 1
        print "Some_var in %s is %d" % (self.name, some_var)
        lock.release()

def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print "After 50 modifications, some_var should have 50"
    print "After 50 modifications, some_var has %d" %(some_var)

use_increment_thread()

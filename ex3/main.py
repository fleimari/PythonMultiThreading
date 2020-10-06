"""Exercise 3.

Write a Python program that has separate function (method) that increases a value of 
global variable count and prints the text "Hello World". The program must have a separate 
main() function that starts the execution of threads and it must have at least two separate threads. 
The thread should be implemented as separate function hello_world() and when program is run, 
the printing of value should be in increasing order (i.e. 1, 2, 3, 4) no matter how many 
instances of the thread hello_world() are started simultaneously in main function. 
(hint you must use some method of synchronization i.e. Lock, Semaphore, Monitor etc.) 
The console output should look similar than in exercise 1 but you may add some features 
to console output that show the state of execution i.e.:

Inside hello_world()
Lock Acquired
Hello World: 1
Inside hello_world()
Lock Acquired
Hello World: 2
"""

import threading
import time

counter = 0                     #Global variable

class MyClass(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        threadLock.acquire()
        print("Thread locked!")
        time.sleep(0.2)

        print("Hello thread:", self.name)
        time.sleep(1)

        threadLock.release()
        print("Thread released!")
        time.sleep(0.2)

threadLock = threading.Lock()

while counter < 10:             #Loop thread
    thread = MyClass(counter)
    thread.start()
    counter = counter + 1
    thread.join()

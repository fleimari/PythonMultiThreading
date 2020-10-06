""""
Exercise 2.

Write similar program than in exercise 1 but this time use
subclass of Thread of threding module and hello_world() -function
printing the text should be member function (method) of class you created.
The console output should look similar than in exercise 1.

Hello World: 0
Hello World: 2
Hello World: 1
Hello World: 3
"""
import threading

class MyThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Hello world from thread", self.name, "!")

thread0 = MyThread("0")
thread1 = MyThread("1")
thread2 = MyThread("2")
thread3 = MyThread("3")

thread0.start()
thread1.start()
thread2.start()
thread3.start()

thread0.join()
thread1.join()
thread2.join()
thread3.join()

print("Completed")
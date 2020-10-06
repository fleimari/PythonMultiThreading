""""
Exercise 1.

Write a Python program that creates thread instance of function hello_world()
that prints out the text "Hello World" four times to console and also prints
out to the console the number of the thread printing the text.

The console output should look like following:

Hello World: 0
Hello World: 2
Hello World: 1
Hello World: 3
"""
import threading

def helloWorld(i):
    print("Hello world from thread {}".format(i))


for i in range(4):
    thread = threading.Thread(target=helloWorld, args=(i,))
    thread.start()

print("Completed!")
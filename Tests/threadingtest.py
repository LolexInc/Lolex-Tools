import threading
def MyThread1():
    firstinput = input("Hello!")
def MyThread2():
    firstinput = input("NUM...")
t1 = threading.Thread(target=MyThread1, args=[])
t2 = threading.Thread(target=MyThread2, args=[])
t1.start()
t2.start()

import threading

def fun1():
    while True:
        print("a")

def fun2():
    while True:
        print("b")

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)


t1.start()
t2.start()


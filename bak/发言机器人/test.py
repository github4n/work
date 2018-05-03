import threading
import time
class A():
    aa = ""
         
class tt(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            a.aa = raw_input('enter:')
            if a.aa=='Q':
                break
def main():
    my_t = tt()
    my_t.start()
    while True:
        if a.aa=="A":
            continue
        elif a.aa=="Q":
            break
        else:
            print('hello',a.aa)
            time.sleep(1)
a = A()
main()
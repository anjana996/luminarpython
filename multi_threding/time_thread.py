from threading import *
import time

def square():
    for n in num:
        time.sleep(1)
        print(n**2)

def double():
    for n in num:
        time.sleep(1)
        print(2*n)


num=[1,2,3,5,9]
begintime=time.time()
print("begintime",begintime)
# t1=Thread(target=square(),args=(num,))
# t1.start()
# t2=Thread(target=double(),args=(num,))
# t2.start()
#
# t1.join()
# t2.join()

endtime=time.time()
print("endtime",endtime)
totaltime=endtime-begintime
print("totaltime",totaltime)
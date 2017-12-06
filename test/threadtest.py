import threading, time
threading.Event()


def count(n):
    inp = n
    start = time.time()
    while n>0:
        n-=1
    else:
        stop = time.time()
        print("%s count done!"%inp,"time:",stop-start)
t = threading.Thread(target=count,args=(10000000,))

t1 = threading.Thread(target=count,args=(100000000,))
t.start()
t1.start()




# def run1():
#     print("grab the first part data")
#     lock.acquire()
#     global num
#     num += 1
#     lock.release()
#     return num
#
#
# def run2():
#     print("grab the second part data")
#     lock.acquire()
#     global num2
#     num2 += 1
#     lock.release()
#     return num2
#
#
# def run3():
#     lock.acquire()
#     res = run1()
#     print('--------between run1 and run2-----')
#     res2 = run2()
#     lock.release()
#     print(res, res2)
#
#
# if __name__ == '__main__':
#
#     num, num2 = 0, 0
#     lock = threading.RLock()
#     for i in range(3):
#         t = threading.Thread(target=run3)
#         t.start()
#
# while threading.active_count() != 1:
#     print("Active:",threading.active_count())
# else:
#     print('----all threads done---')
#     print(num, num2)



# st=time.time()
# t_obj=[]
# for i in range(50):
#     t1 = threading.Thread(target=sayhai, args=("t-%s"%i,))
#     t1.setDaemon(True)
#     t1.start()
#     t_obj.append(t1)
#
# sto=time.time()
# print(sto-st,threading.current_thread())
# print(t1.getName(),t2.getName())
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#     def run(self):
#         print("running on numbers:", self.num)
#         time.sleep(3)
# t1=MyThread(1)
# t2=MyThread(2)
# t1.start()
# t2.start()
# print(t1.getName(),t2.getName())
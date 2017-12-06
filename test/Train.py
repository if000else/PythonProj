import queue,threading,time,random

event = threading.Event()
line = queue.Queue(4)

def train(name):
    try:
        while True:
            if line.full():
                print("\033[31;1m No available stop!!!\033[0m")
                print("There are\033[31;1m %s \033[0m stop available." % line.qsize())
                time.sleep(0.5)
            else:
                print("There are\033[31;1m %s \033[0m stop available." % line.qsize())
                line.put_nowait(name)
                print("Train\033[33;1m %s is in...\033[0m" % name)
                break

        time.sleep(5)
        line.get(True)
        print("Train\033[32;1mTrain %s is out...\033[0m"%name)
    except Exception as e:
        print("error:",e)

for i in range(100):
    num = "No.%s"%i
    t = threading.Thread(target=train,args=(num,))
    t.start()
    time.sleep(random.randint(1,2))


import sys,time
start = 1
stop = 100
while start <= stop:
    sys.stdout.write('\r[')
    percet = 100 * start / stop
    sys.stdout.write(('%s%%'%percet).rjust(int(percet/2+5),'='))
    sys.stdout.write(']')
    sys.stdout.flush()
    start += 1
    time.sleep(0.1)
else:
    print("complete!")
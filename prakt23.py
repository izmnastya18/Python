from threading import Thread
import time
time1=()
time2=()
xy = [50, 437, 34, 763, 2487, 30094, 5999, 5, 2] 
def func1(a,b):
    global xy
    global time1
    result_min1=max(xy)
    # print(result_min1,'- это 1 поток')
    time.sleep(1)
    time1=time.time(),"1"
    print(time1)
    return result_min1 

def func2(c,n):
    global xy
    global time2
    count=0
    for i in xy:
        if i>count:
            count=i
    # print(count,'- это 2 поток')               
    time.sleep(1)
    time2=time.time(),'2'
    print(time2)
    return count


if __name__ == '__main__':
    Thread(target = func1,args=(1,8)).start()
    Thread(target = func2,args=(4,7)).start()
    if time1<time2:
        print('1 быстрее выполняет ')
    elif time1==time2:
        print('одинаковое быстродействие')
    else:
        print('2 быстрее выполняет')

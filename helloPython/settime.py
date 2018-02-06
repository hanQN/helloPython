
#-*- coding:utf-8 -*-

#定时任务
import datetime, os, platform
from twisted.python.runtime import seconds


def run_Task():
    os_platfrom = platform.platform()
    if os_platfrom.startswith('Darwin'):
        print 'this is mac od system'
        #os.system('ls')
    elif os_platfrom.startswith('Window'):
        print 'this is win system'
        #os.system('dir')
        
    
def timerFun(sched_Timer):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now==sched_Timer and flag==0:
            print sched_Timer,'***',now
            #run_Task()
            print 'heihiehiehie'
            flag = 1
        else:
            if flag == 1:
                sched_Timer = sched_Timer + datetime.timedelta(seconds=5)
                flag = 0

if __name__ == '__main__':
    now = datetime.datetime.now()
    sched_Timer = now #datetime.datetime(2017,12,4,11,26,0)
    print sched_Timer
    print 'run the timer task at {0}'.format(sched_Timer)
    timerFun(sched_Timer)
    

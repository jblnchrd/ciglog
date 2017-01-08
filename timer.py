#timer.py
import sys
import winsound
from time import time, sleep

def set_timer(alarm_time):
    time_now = int(time())
    times_up = False
    sleep_for = int(alarm_time) - int(time_now)
    assert(sleep_for > 0)
    sleep(sleep_for)
    for i in xrange(4):
        winsound.Beep(1100, 900)

    
    
if __name__ == "__main__":
        arg = sys.argv
        assert(len(arg) > 1)
        t = int(arg[1])
        set_timer(t)
        exit()

# time functions
import filehandler

def time_diff(a, b): #Terrible code to subtract times. But hey, it works...
    ans = [0,0,0]
    ans2 = [0,0,0]
    c = [23,60,60]
    #time a followed by time b.
    assert(len(a) == len(b))
    if(b[0] > a[0]):
        for i in range(2, 0, -1):
            if(b[i] < a[i]): #must carry
                ans[i] = (b[i] + 60) - a[i]
                b[i-1] -= 1
            else:
                ans[i] = b[i] - a[i]
        ans[0] = b[0] - a[0]
        return ans

    elif(b[0] < a[0]):
        for i in range(2, 0, -1):
            if(a[i] < b[i]):
                ans[i] = (a[i]+60) - b[i]
                a[i-1] -= 1
            else:
                ans[i] = a[i] - b[i]
        ans[0] = a[0] - b[0]  
        for i in range(2, -1, -1):
            #subtract a from c (c-a)
            ans2[i] = c[i] - ans[i]
        return ans2

    else: #hours are equal
        for i in range(2, 0, -1):
            if(b[i] < a[i]):
                ans[i] = (b[i] + 60) - a[i]
                b[i-1] -= 1
            else:
                ans[i] = b[i] - a[i]
        return ans

        
def seconds_to_format(seconds):
    l = ()
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    l = (hour, min, sec)
    return l
    
    
def avg_time(logf):
    utimes = utimes_to_list(logf)
    utimes = filter(lambda a: a != 0.0, utimes)
    #print("utimes: {}".format(utimes))
    ntimes = len(utimes)
    time_diffs = []
    total = 0.
    
    for i in xrange(ntimes - 1, 0, -2):
        if (i-1 >= 0):
            time_diffs.append(float(utimes[i]) - float(utimes[i-1]))
    #print("time_diffs: {}".format(time_diffs))
    for j in range(len(time_diffs)):
        total += time_diffs[j]
    avg = total / float(len(time_diffs))
    #print(avg)
    formatted = seconds_to_format(avg)
    return formatted #a tuple
    
def utimes_to_list(logf):
    f = filehandler.file_to_list(logf)
    times = []
    for log in f:
        times.append(get_utime(log))
    return times
 
 
def get_utime(entry):
    if(entry[25:] != ''):
        ut = entry[25:]
        return float(ut)
    return 0.

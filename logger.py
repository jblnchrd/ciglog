"""
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


import sys
from time import *
import os.path


def add_entry(file_):
	time_stamp = str(ctime())
	file_.write('{} {}'.format(time_stamp, time()))
	file_.write("\n")
	file_.close()

def utimes_to_list():
    logs = load_log()
    times = []
    for log in logs:
        times.append(get_utime(log))
    return times

def make_log_file():
    f = open("C:\\Users\\tharoot\\Documents\\pyciglogs.txt", "w")
    add_entry(f)
    print("remember: Enter m as arg for menu.")



def get_last():
    ents = []
    ents = load_log()
    last = ents[-1]
    return last



def diff_gen(t1, t2):#strings t1, t2
    
    x = t1.split(":")
    y = t2.split(":")
    T1 = [int(i) for i in x]
    T2 = [int(i) for i in y]
    T1[0] = T1[0] % 12
    T2[0] = T2[0] % 12
    assert(len(T1) == len(T2))
    total = []
    total = time_diff(T1, T2)
    assert(len(total) == 3)
    return total



def print_diff():
# probably the ugliest, worst code ever.rework this.
    ents = load_log()
    last_times_ents = ents[-2:]
    final_ents = " ".join(last_times_ents).split(" ")
    #print("Testing---- times:{}".format(final_ents))
    times = []
    for i in final_ents:
        if(':' in i):
            times.append(i)
    times = ":".join(times).split(":")
    nums = [int(i) for i in times]
    first = nums[:3]
    first[0] = first[0] #% 12
    second = nums[3:]
    second[0] = second[0] #% 12
    assert(len(first) == len(second))
    ans = []
    ans = time_diff(first, second)
    print("{} hrs, {} mins, {} sec".format(ans[0],ans[1],ans[2]))
    return ans
  

def get_utime(entry):
    if(entry[25:] != ''):
        ut = entry[25:]
        return float(ut)
    return 0.


def print_diff_now():
    ents = load_log()
    last_time = ents[-1]
    last = last_time[11:19]
    current_time = ctime()[11:19]
    now = current_time.split(":")
    final = last.split(":")
    now_n = [int(i) for i in now]
    final_n = [int(i) for i in final]
    now_n[0] = now_n[0] #% 12
    final_n[0] = final_n[0] #% 12
    assert(len(now_n) == len(final_n))
    total = []
    #for i in range(len(now_n)):
    total = time_diff(final_n, now_n)
    assert(len(total) == 3)
    print("{t[0]}:{t[1]}:{t[2]} since last smoke.".format(t=total))



def to_seconds(lst):
    seconds = 0
    for n in range(len(lst)):
        if(n == 0):
            seconds += lst[n]*3600.
        else:
            seconds += lst[n]*60.
    return seconds


def seconds_to_format(seconds):
    l = ()
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    l += (hour, min, sec)
    return l


#needs work. I think.
def time_diff(a, b): #Terrible code to subtract times, waay too long. But again, it works...
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



def avg_time(logf):
    utimes = utimes_to_list()
    ntimes = len(utimes)
    time_diffs = []
    total = 0.
    i = 0
    for i in xrange(ntimes-1, 2, -2):
        if (i-1 >= 1):
            time_diffs.append(utimes[i] - utimes[i-1])
            
    for j in range(len(time_diffs)):
        total += time_diffs[j]
    avg = total / float(len(time_diffs))
    formatted = seconds_to_format(avg)
    return formatted #a tuple


def show_usage():
    print("USAGE\n\n[-n]:\tDifference now\n[-c]:\tchange log file\n\
    [-a]:\taverage\n[-d]:\tdifference\n[-l]:\tshow last\n[-p]:\tavg per day\n[-z]:\tnew log\n")
    print("Execute the program without arguments to add an entry to the log.")

def load_log(fname=""):
    log = open(fname, "r")
    lines_list = log.readlines()
    log.close()
    return lines_list



def menu(opt, fname):
    
    if ('-' in opt):
        if('h' in opt):
            show_usage()
        else:
            if('t' in opt):
                print(get_last())
                             
            if('d' in opt):
                print_diff()
                           
            if('n' in opt):
                print_diff_now()
                
            if('a' in opt):
                avg = avg_time(fname)
                l = []
                for i in avg:
                    l.append(int(i))
                print("Average seconds between logs: {t[0]}:{t[1]}:{t[2]}".format(t=l))
    else:
        print("Remember to place a - in front of all arguments")
        show_usage()
        


# ctime()[11:19] returns the time only from the string...
def main():
    fname = ""
    f = open("fname", "a")
    args = sys.argv
    if (os.path.isfile(fname) and len(args) == 1):
        add_entry(f)
    elif (len(args) > 1):
        menu(args[1])
    else:
        really = raw_input("Are you sure you wish to create new log file?")
        if(really == "y" or really == "Y"):
            really2 = raw_input("This may overwrite your current log file. Are you really sure?")
            if(really2 == "y" or really2 == "Y"):
                print("Fine...Making a new log file.")
                make_log_file()
            else:
                f.close()
                exit()
        else:
            f.close()
            exit()
    f.close() #just to be sure...
    exit()


if __name__ == '__main__':
	main()


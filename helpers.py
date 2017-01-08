#Helper functions....
import filehandler
import mtime
import logger
from time import *


def show_usage():
    with open("C:\\Users\\tharoot\\Documents\\ciglogger\\help.txt", 'r') as help:
        f = list(help)
        for line in f:
            print(line)
    
    
    
def menu(opt, f):
    fname = filehandler.get_config_file()
    assert(f == fname)
    #print("f is fname!")
    if ('-' in opt):
        if('h' in opt):
            show_usage()
        else:
            if('l' in opt):
                if(logger.add_ent()):
                    print("added log!")
                    exit()
                else:
                    print("An error ocurred...")
            if('t' in opt):
                print("Current time is {}".format(time()))
                import subprocess
                atime = raw_input("Enter seconds for timer: ")
                try:
                    t = int(atime) + int(time())
                except ValueError:
                    print("Must enter an integer!")
  
                print("starting timer process...")
                arg = str(t)
                subprocess.Popen("python ./timer.py " + arg, shell=True)
                print("Timer started...")
                
            if('s' in opt):
                filehandler.print_log(f)
                
            if('r' in opt):
                if(logger.remove_last(f)):
                    print("Remove Successful.")

            if('g' in opt):
               print(filehandler.get_last(f))

                           
            if('n' in opt):
                print_diff_now(f)
                
            if('a' in opt):
                avg = mtime.avg_time(f)
                print("Average time between logs: {0}:{1}:{2}".format(int(avg[0]), int(avg[1]), int(avg[2])))
    
            if('q' in opt):
                mtime.print_per_date(f)
            
    else:
        print("Remember to place a - in front of all arguments")

        show_usage()
        
def print_diff_now(fname, nonmil=False):
    ents = filehandler.file_to_list(fname)
    last_time = ents[-1]
    last = last_time[11:19]
    current_time = ctime()[11:19]
    now = current_time.split(":")
    final = last.split(":")
    now_n = [int(i) for i in now]
    final_n = [int(i) for i in final]
    if(nonmil):
        now_n[0] = now_n[0] % 12
        final_n[0] = final_n[0] % 12
    assert(len(now_n) == len(final_n))
    total = []
    #for i in range(len(now_n)):
    total = mtime.time_diff(final_n, now_n)
    assert(len(total) == 3)
    print("{}:{}:{} since last smoke.".format(total[0], total[1], total[2]))
    

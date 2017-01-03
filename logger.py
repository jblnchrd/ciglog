# logger
from time import *
import filehandler
    
def add_ent():
    time_stamp = "\n"+str(ctime())
    file_ = filehandler.get_config_file()
    now = time()
    if(filehandler.append_file(file_, time_stamp)):
        filehandler.append_file(file_, " {}".format(now))
        return 1
    return 0
        
def remove_last(logf):
    l = filehandler.file_to_list(logf)
    print("l: {}".format(l))
    assert(l is not None)
    last_line = len(l)
    del l[last_line - 1]
    if(filehandler.write_to_file(logf, l)):
        return 1
    return 0
    
# Filehandler.py

def file_to_list(fname):
    with open(fname, 'r') as fObj:
        l = list(fObj)
        return l
    return 0

    
def get_config_file():
    lines = file_to_list("config.txt")
    for line in lines:
        if "file=" in line:
            return line[len("file="):]
    return 0


def update_config_file(name):
    lines = file_to_list("config.txt")
    
    with open("config.txt", "a+"):
        for line in lines:
            if "file:" in line:
                config.write("file={}".format(name))
                return 1
    return 0


def make_log_file(filename=get_config_file()):
    with open(filename, "w") as f:
        import logger
        logger.add_entry(f)
        return 1
    return 0


def get_last(fname):
    list = file_to_list(fname)
    return list[-1]
    

 
def write_to_file(fname, data):
    with open(fname, "w") as fObj:
        for n in data:
            fObj.write(n)
        return 1
    return 0

    
def append_file(fname, data):
    read = file_to_list(fname)
    with open(fname, "a") as fObj:
        fObj.write(data)
        return 1
    return 0
    
def print_log(fname):
    f = file_to_list(fname)
    for line in f:
        print(line)

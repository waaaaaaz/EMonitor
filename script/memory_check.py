import time

def get_linux_freemem():
    ''' Grab memory stats for Linux systems '''
    memstats = {}
    with open("/proc/meminfo", "r") as fh:
        for entry in fh.readlines():
            key, value = entry.split(":")
            value = value.split()[0]
            #memstats[key] = float(value)
            memstats[key] = float(value)
    if "MemAvailable" in memstats:
        return (memstats['MemAvailable'] / memstats['MemTotal']) * 100.00
    else:
        ## Linux Free Memory Calculation
        return ((memstats['MemFree'] + memstats['Buffers'] + memstats['Cached']) /
                memstats['MemTotal']) * 100

def getMem(): 
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1]) 
        free = int(f.readline().split()[1]) 
        buffers = int(f.readline().split()[1]) 
        cache = int(f.readline().split()[1]) 
        mem_use = total-free-buffers-cache 
        return mem_use/1024


if __name__ == '__main__':
#    while True:
#        time.sleep(1)
#        print round(get_linux_freemem()), "%"

    #print "{}\%  memory used".format(str(round(get_linux_freemem())))
    print round(get_linux_freemem()), "% ", "memory available."
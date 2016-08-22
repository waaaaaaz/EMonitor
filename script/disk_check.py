# coding: utf-8

import subprocess
import sys


def disk_free_linux():
    ''' check filesystem usage '''
    result = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE).communicate()[0]
    if result:
        disk_usage = {}
        for line in result.splitlines()[1:]:
            disk_usage[line.split()[0]] = line.split()[4]
        print disk_usage
    else:
        print "DISK_FREE UNKNOWN Error pulling disk information {0}".format(e.message)
        sys.exit("3")


if __name__ == '__main__':
    disk_free_linux()
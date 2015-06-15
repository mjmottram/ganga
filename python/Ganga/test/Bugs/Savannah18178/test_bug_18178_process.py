#!/usr/bin/env python

import sys,os,time

if len(sys.argv)>1:
    pid = os.fork()

    if pid == 0:
        while 1:
            time.sleep(5)
    else:
        f = file(sys.argv[1]+'/proc_stat','w')
        f.write(str(pid))
        f.close()
        os.wait()

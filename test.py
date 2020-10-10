import curses
import time 

import sys

while True:
    sys.stdout.write("\r" + time.ctime())
    sys.stdout.flush()
    time.sleep(1)


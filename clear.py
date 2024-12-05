import sys
import os
import time

try:
    while True:
        print("foo")
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
except KeyboardInterrupt:
    sys.exit()

    

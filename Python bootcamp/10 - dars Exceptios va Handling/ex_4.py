from datetime import datetime
import time

try:
    while True:
        now = datetime.now()
        print(now.strftime("%X"))
        time.sleep(2)   
except KeyboardInterrupt:
    print("stopped")

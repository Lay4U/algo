import time
from datetime import datetime

import win32api
import winsound

frequency = 1500
duration = 100


def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


while True:
    now = datetime.now()
    print(now, getIdleTime())
    if getIdleTime() > 3600:
        time.sleep(60)
        continue
    elif now.minute == 50:
        print(now)
        print(getIdleTime())
        winsound.Beep(frequency, duration)

    time.sleep(60)

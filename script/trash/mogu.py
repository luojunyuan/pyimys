from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import datetime
import platform
import ctypes
import time
import sys
import os
TIMEOUT = 10
button = {
    'mogu1':(770, 680),
    'mogu2':(770, 600)
}

def click(word, time):

    x, y = button[word]
    device.touch(x, y, 'DOWN_AND_UP')
    MonkeyRunner.sleep(time)

def init():

    print('Connecting...')
    start = time.time()
    device = MonkeyRunner.waitForConnection(TIMEOUT)
    end = time.time() - start
    if end >= TIMEOUT:
        print('Connect failed')
        sys.exit(1)
    else:
        print('Success connect default phone!')

    return device

def script():
    while(True):
        click('mogu1', 1)
        click('mogu2', 1)
        click('mogu2', 1)

if __name__ == '__main__':
    device = init()
    script()
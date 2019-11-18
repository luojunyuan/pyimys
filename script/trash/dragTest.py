# -*- coding: UTF-8 -*-
'''
    查看列表顺序：（19.1.11）精花*4->钱*4->日常*n (dimond-4)
    使用方法：点击超级钱No.1 切换到猫队，修改dimond为钻石本数目-4
    过程：开始挂机，配合caffine使用保证win10不休眠，打完钱自动切换到主队
    代码：不添加非asc字符作为文件名或变量，添加code--utf-8
'''
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import platform
import ctypes
import time
import sys
import os

# old path | os.environ.get('ANDROID_HOME') + '\\tools\\source\\'
RS_PATH = 'C:\\Users\\ljy77\\Documents\\imys\\source\\'
TIMEOUT = 10
DEAFUALT_HALF = 0.5
device = None
# dimond is all mission - 4 flower - 4 money - 4 last
dimond = 7
wait = MonkeyRunner.loadImageFromFile(RS_PATH + 'waitScrn.png')
quest = MonkeyRunner.loadImageFromFile(RS_PATH + 'battle_list.png')
againPage = MonkeyRunner.loadImageFromFile(RS_PATH + 'againPage.png')
lvup = MonkeyRunner.loadImageFromFile(RS_PATH + 'lvup.png')
noBP = MonkeyRunner.loadImageFromFile(RS_PATH + 'noBP.png')
firCls = MonkeyRunner.loadImageFromFile(RS_PATH + 'clear.png')
failed = MonkeyRunner.loadImageFromFile(RS_PATH + 'failed.png')
# wavePause = mr.loadImageFromFile('C:\\Users\\ljy77\\AppData\\Local\\Android\\android-sdk\\tools\\source\\waveMid.png')

k = { 'again':  (1020, 1000),
      'next' :  (1700, 1000), 
      'start':  (1500, 1000),
      #add y 150
      'quest1': (300, 200),
      'quest2': (300, 350),
      'quest3': (300, 500),
      'quest4': (300, 650),
      'quest5': (300, 800),
      #auto click quest 2
      'questAuto':(300, 350),
      'stage':  (1170, 830),
      'close-c':( 950,  800),#first clear
      'close-u':( 950,  770),#lv up
      '1-1:':    (   0,    0),
      'back':    ( 100,   60),
      'HOME':    ( 100, 1000),
      'blank_title':(960, 65),
      'left_switch':(220,1000),
      'right_switch':(1100,990)
}

def click(word, delay):
    x, y = k[word]
    device.touch(x, y, 'DOWN_AND_UP')
    MonkeyRunner.sleep(delay)

def isScreen(png, similarity):
    return device.takeSnapshot().sameAs(png, similarity)

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

    # device.drag((300, 800), (300, 650), 0.7, 10)
    # MonkeyRunner.sleep(1)
    # click('quest5', 1)
    start = time.time()
    device.drag((300, 800), (300, 650), 0.9, 10)   
    MonkeyRunner.sleep(1.5)
    end = time.time() - start
    print(end)

if __name__ == '__main__':
    # device = MonkeyRunner.waitForConnection()
    # device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

    # print("Fake script")
    # dimond = int(input('input dimond mission num >_'))
    device = init()
    script()
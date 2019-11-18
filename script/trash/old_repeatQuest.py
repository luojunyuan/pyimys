# adb connect 192.168.50.23:5555
# adb connect 192.168.50.27:7555
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import datetime
import platform
import ctypes
import time
import sys
import os

USE_BP = True
RS_PATH = 'C:\\Users\\ljy77\\Desktop\\library\\pyimys\\script\\monkeyImys\\source\\'
debug_mode = False
TIMEOUT = 10
DEAFUALT_HALF = 0.5

wait = MonkeyRunner.loadImageFromFile(RS_PATH + 'loading.png')
quest = MonkeyRunner.loadImageFromFile(RS_PATH + 'quest.png')
againPage = MonkeyRunner.loadImageFromFile(RS_PATH + 'result_panel.png')
noBP = MonkeyRunner.loadImageFromFile(RS_PATH + 'noBP.png')
failed = MonkeyRunner.loadImageFromFile(RS_PATH + 'failed.png')

lvup = MonkeyRunner.loadImageFromFile(RS_PATH + 'lvup.png')
firCls = MonkeyRunner.loadImageFromFile(RS_PATH + 'first_reward.png')

# wavePause = mr.loadImageFromFile('C:\\Users\\ljy77\\AppData\\Local\\Android\\android-sdk\\tools\\source\\waveMid.png')
# bpRec = MonkeyRunner.loadImageFromFile(RS_PATH + 'bp_recover.png')

k = { 
        'start':(950, 666),
        'stage':(779, 553),
        'close-c':(633, 533),#first clear
        'close-u':(633, 513),#lv up
        '1-1:':(0, 0),
        'back':(66, 39),
        'HOME':(66, 666),
        'blank_title':(639, 43),
        'bp_recive':(500, 450),
        'confirm_use':(760, 500),
        'confirm_close':(640, 490),
        'again':(770, 680),
        'meowaza':(75, 320),
        'heal':(440,200),
        'sword':(470,540),
        'hado':(1000,660)
}

k_old = {'again':        (1020, 1000),
      'start':        (1500, 1000),
      'stage':        (1170, 830),
      'close-c':      ( 950,  800),
      'close-u':      ( 950,  770),
      '1-1:':         (   0,    0),
      'back':         ( 100,   60),
      'HOME':         ( 100, 1000),
      'blank_title':  (960, 65),
      'bp_recive':    (740,  678),
      'confirm_use':  (1143,751),
      'confirm_close':(958,734),
}

def click(word, time):
    x, y = k[word]
    device.touch(x, y, 'DOWN_AND_UP')
    MonkeyRunner.sleep(time)

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

def loadScrn():

    #wait for loding message
    # while not isScreen(wait, 0.3):
    #     if debug_mode:
    #         print('not blank page')
    #     MonkeyRunner.sleep(0.5)

    #wait for tips picture
    while isScreen(wait, 0.3):
        if debug_mode:
            print('is blank page')
        MonkeyRunner.sleep(1)

    #tail work
    MonkeyRunner.sleep(1)

def loop():

    if isScreen(quest, 0.4):
        if debug_mode:
            print('sending start!')
        click('start', 1)
    #again page
    else:
        if debug_mode:
            print('push button again!')
        click('again', 1)
        if isScreen(lvup, 0.08):
            print('Congradulation! level up!')
            click('close-u', 1)
            click('again', 1)
        if isScreen(noBP, 0.5):
            if USE_BP:
                print('Low BP... Use BP medicine!')
                click('bp_recive', 1)
                click('confirm_use', 2)
                click('confirm_close', 1)
                return 0
            print('Low BP... All done')
            print('current time is '+ datetime.datetime.now().strftime('%H:%M:%S'))
            # caculate as 40/450 bp left
            # (450 - 40)/60 
            # time + 6:50
            sys.exit(0)
        # if isScreen(firCls, DEAFUALT_HALF):
        #     if debug_mode:
        #         print('turndown recive page')
        #     click('close-c', 1)
        #     click('again', 1)
        
    # if debug_mode:
    #     print('ready to load screen')

    # loadScrn()

    if debug_mode:
        print('we are in battle')
    # battle
    # just wait for moewaza
    MonkeyRunner.sleep(6)

    #use meo waza
    # click('meowaza', 1)
    # click('sword', 1)
    # click('hado', 1)

    count = 1
    while not isScreen(againPage, 0.35):
        MonkeyRunner.sleep(1)
        # to keep screen awake
        count += 1
        if debug_mode:
                print('battle count:'+str(count))
        if count == 10:
            click('meowaza', 1)
            click('heal', 1)
            click('hado', 1)
            
        if count % 30 == 0:
            click('blank_title', 0.1)
            #use moe waza
            # if count == 60:
            #     click('meowaza', 1)
            #     click('heal', 1)
            #     click('hado', 1)
            #     break

        if isScreen(failed, 0.2):
            print('loop failed')
            click('stage', 1)
            if debug_mode:
                print('load screen')
            loadScrn()
            break
            
    for i in range(0, 10):
        click('blank_title', 0.1)
    for i in range(0, 10):
        click('blank_title', 0.1)
    for i in range(0, 10):
        click('blank_title', 0.1)

    if debug_mode:
        print('this turn is over!')    
    # tail work
    MonkeyRunner.sleep(1)

def script():
    i = 1
    while(True):
        print('Processing loop ' + str(i) + ' ...')
        loop()
        i += 1


if __name__ == '__main__':
    device = init()
    script()
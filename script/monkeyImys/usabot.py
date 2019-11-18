from com.android.monkeyrunner import MonkeyRunner
from buttonMap import button
from image import *
import datetime
import time
import sys

class Usabot:

    def __init__(self, config):

        self.TIMEOUT = config.TIMEOUT
        self.DEBUG_SIGNAL = config.DEBUG_SIGNAL
        self.BP_SIGNAL = config.BP_SIGNAL
        self._DEBUG('INFO','debug initialization')
        self.device = self.getDevice()
        self.week = self._getWeek()


    def getDevice(self):

        self.shaberu('usa link chu...')
        start = time.time()
        device = MonkeyRunner.waitForConnection(self.TIMEOUT)
        end = time.time() - start
        if end >= self.TIMEOUT:
            self.shaberu('failed, usa cry(\';w;`)')
            sys.exit(1)
        else:
            self.shaberu('usa standby ready!')

        return device


    def tap(self, word, time):
        '''
            word:str button name, reference to buttonMap.py
            time:int tap wait time
        '''
        x, y = button[word]
        self.device.touch(x, y, 'DOWN_AND_UP')
        MonkeyRunner.sleep(time)
    

    def shaberu(self, kotoba):
        
        print(kotoba)

    
    def usaWait(self, time):

        return MonkeyRunner.sleep(time)


    def circle(self):
        '''
            process one circle
            bad way
            2 sometimes loading page is too long, or loding bar
            3 click will go fast
        '''
        self._DEBUG('INFO', 'start circle()')
        while True:
            if self.match('IMAGE_Quest'):
                self.tap('start', 1)
                break
            elif self.match('IMAGE_Result'):
                self.tap('again', 1)            
                break

        timecount = 0

        while not self.match('IMAGE_Result'):
            self._DEBUG('VARIABLE', 'circle time count: '+str(timecount))
            self.usaWait(1)
            if self.match('IMAGE_Failed'):
                self._DEBUG('WARN', 'circle failed')
                self.tap('stage', 1)
                return 

            timecount += 1

        self._DEBUG('INFO', 'match rusult panel')

        # for i in range(0, 10):
        #     self.tap('blank_title', 0.1)
        # for i in range(0, 10):
        #     self.tap('blank_title', 0.1)
        # for i in range(0, 10):
        #     self.tap('blank_title', 0.1)
        while not self.match('IMAGE_Fircls'):
            self.usaWait(1)
            
        self._DEBUG('INFO', 'match reward panel')
        self.tap('blank_title', 2)
        self.tap('over', 1)
        while not self.match('IMAGE_Quest'):
            self.usaWait(1)
        self._DEBUG('INFO', 'match quest list')
        self._DEBUG('INFO', 'over circle()')

    
    def moewaza(self, waza, timecount):

        pass


    def match(self, position):
        '''
            ensure curent position
        '''
        if position == 'IMAGE_Loding':
            return self._checkPosition(IMAGE_Loding, 0.3)
        elif position == 'IMAGE_Result':
            return self._checkPosition(IMAGE_Result, 0.35)
        elif position == 'IMAGE_Lvup':
            return self._checkPosition(IMAGE_Lvup, 0.08)
        elif position == 'IMAGE_NoneBP':
            return self._checkPosition(IMAGE_NoneBP, 0.5)
        elif position == 'IMAGE_Fircls':
            return self._checkPosition(IMAGE_Fircls, 0.5)
        elif position == 'IMAGE_Failed':
            return self._checkPosition(IMAGE_Failed, 0.2)
        elif position == 'IMAGE_Quest':
            return self._checkPosition(IMAGE_Quest, 0.4)
        pass


    def _checkPosition(self, png, similarity):

        return self.device.takeSnapshot().sameAs(png, similarity)


    def _loadScrn(self):

        #wait for loding message
        # while not isScreen(wait, 0.3):
        #     MonkeyRunner.sleep(0.5)

        #wait for tips picture
        while self.match('IMAGE_Loding'):
            MonkeyRunner.sleep(1)

        #tail work
        MonkeyRunner.sleep(1)


    def _getWeek(self):
        '''
            0-6 -> monday-sunday
        '''
        weekday = (datetime.datetime.now() + datetime.timedelta(hours=1)).weekday()
        return weekday


    def _DEBUG(self, level, message):

        if self.DEBUG_SIGNAL:
            time = datetime.datetime.now().strftime('%X')
            print(time + ' ' + level + ' ' + message)    


    def _tap(self, word, time):
        '''
            original adb tap
        '''
        x, y = button[word]
        pass


    def _saveResult(self):
        pass
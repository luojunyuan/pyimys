# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr, MonkeyDevice as md, MonkeyImage as mi
import sys
import os
device = mr.waitForConnection(10)

def save_screenshot_to_desktop(name):
    '''
        receive a name(string)
        output an png on desktop
    '''
    name = name.decode('utf-8')+'.png'
    pic = device.takeSnapshot()
    pic.writeToFile('C:\\Users\\ljy77\\Desktop\\'+name.decode('utf-8'))

def compare_screenshot_and_localPicture(image, similar = 0.5):
    '''
        recive a picture and similar, print is matched
        default similar: 0.5
    '''
    pic = device.takeSnapshot()
    if pic.sameAs(image, similar):
        print(str(similar)+' similar is matched')
    else:
        print('bu xiang si')

def caculate_screenshot_and_localPicture_similar(image):
    '''
        give a local picture, print the similar with snapshot
    '''
    pic = device.takeSnapshot()
    l = 0
    h = 1.0
    for i in range(0, 5):
        m = (l + h) / 2
        if pic.sameAs(image, m):
            l = m
        else:
            h = m
    print('similiar ' + str(m))

# absolute path
# os.getcwd 是得到了monkeyrunner的路径
# RS_PATH = 'C:\\Users\\ljy77\\Documents\\imys\\source\\'
# quest = mr.loadImageFromFile(RS_PATH + 'clear.png')
# caculate_shortcut_and_localPicture_similiar()
if __name__ == '__main__':
    filename = 'tmp'
    # filepath = 'C:\\Users\\ljy77\\Documents\\imys\\source\\'+ filename + '.png'
    # image = mr.loadImageFromFile(filepath)
    # create screenshot
    save_screenshot_to_desktop(filename)

    # print similar
    # caculate_screenshot_and_localPicture_similar(image)

    # print is matched
    # compare_screenshot_and_localPicture(image)

# 60 76    1002 88
# 40 1836  1015 1780    
# game
# 108 60   1782 38
# 96 987   1758 1017

#move touch bar similiar go down
#newImys every float is my blood
from com.android.monkeyrunner import MonkeyRunner
import sys

def caculate_screenshot_and_localPicture_similar(device, image):
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

def save_screenshot_to_desktop(device, name):
    '''
        receive a name(string)
        output an png on desktop
    '''
    name = name.decode('utf-8')+'.png'
    pic = device.takeSnapshot()
    pic.writeToFile('C:\\Users\\ljy77\\Desktop\\'+name.decode('utf-8'))
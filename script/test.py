import sys
from com.android.monkeyrunner import MonkeyRunner
sys.path.append('C:\Users\ljy77\Desktop\library\pyimys\script')
from monkeyImys import usabot
from monkeyImys import config
from monkeyImys import tools
from monkeyImys import image
import getopt

if __name__ == "__main__":
    koto = usabot.Usabot(config)
    path = 'C:/Users/ljy77/Desktop/1.png'
    image = MonkeyRunner.loadImageFromFile(path)

    # tools.caculate_screenshot_and_localPicture_similar(koto.device, image.IMAGE_Fircls)
    # tools.caculate_screenshot_and_localPicture_similar(koto.device, image)
    # koto.device.drag((300,900),(200,500),1)
    MonkeyRunner.sleep(1)
    tools.save_screenshot_to_desktop(koto.device, 'share')
from com.android.monkeyrunner import MonkeyRunner
import os
# png image path, only for file in scripts/
PATH = os.path.abspath('monkeyImys') + '\\source\\'
IMAGE_Loding = MonkeyRunner.loadImageFromFile(PATH + 'loading.png')
IMAGE_Quest = MonkeyRunner.loadImageFromFile(PATH + 'quest.png')
IMAGE_Result = MonkeyRunner.loadImageFromFile(PATH + 'result_panel.png')
IMAGE_Lvup = MonkeyRunner.loadImageFromFile(PATH + 'lvup.png')
IMAGE_NoneBP = MonkeyRunner.loadImageFromFile(PATH + 'noBP.png')
IMAGE_Fircls = MonkeyRunner.loadImageFromFile(PATH + 'first_reward.png')
IMAGE_Failed = MonkeyRunner.loadImageFromFile(PATH + 'failed.png')
# wavePause = MonkeyRunner.loadImageFromFile()

# \\ or /
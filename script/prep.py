from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()
device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

print("Fake script is done.")
print("Now turning OFF tablet for actual script.")
print("Please standby...")
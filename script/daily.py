import sys
sys.path.append('C:\Users\ljy77\Desktop\library\pyimys\script')
from monkeyImys import usabot
from monkeyImys import config
import getopt

def main(quest_num):
    koto = usabot.Usabot(config)

    if 0 == quest_num :
        # friday 4 has some problems
        if 5 == koto._getWeek():
            quest_num = 14
        else :
            quest_num = 11

    koto.circle()
    koto.usaWait(2)

    for i in range(0, int(quest_num)-3):
        koto.tap('quest3', 1)
        koto.circle()
        koto.usaWait(2)

    koto.tap('quest4', 1)
    koto.circle()
    koto.usaWait(2)
    koto.tap('quest5', 1)
    koto.circle()
    koto.usaWait(2)

def usage():
    print('usage: monkeyrunner dayily.py [--quest<number>] [-d | --debug] [-h | --help] [--timeout<time>]')
    print('       --timeout: usa connect timeout second, default 10s')
    print('       --quest: to deal special situation, assign rest number of quest')
    print('                quest must big than 3')
    print('       choose quest below last "mogukouka"')
    print('       any dayliy quest must be "new"')

if __name__ == "__main__":
    quest_num = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hd', ['quest=', 'help', 'debug', 'timeout='])
    except getopt.GetoptError:
        print(getopt.GetoptError)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ['-d', '--debug']:
            config.DEBUG_SIGNAL = True
            print('set DEBUG signal true')
        elif opt in ['--timeout']:
            config.TIMEOUT = arg
            print('set TIMEOUT '+arg+'s')
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt in ['--quest']:
            quest_num = arg
            print('set quest numbers '+arg)

    main(quest_num)
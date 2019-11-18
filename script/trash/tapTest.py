import sys
sys.path.append('C:/Users/ljy77/Desktop/library/pyimys/script')
from monkeyImys import usabot
from monkeyImys import config

if __name__ == "__main__":
    koto = usabot.Usabot(config)
    koto.tap('over', 0)
    koto.syaberu('mission finish!')
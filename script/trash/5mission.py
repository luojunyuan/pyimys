import sys
sys.path.append('C:/Users/ljy77/Desktop/library/pyimys/script')
from monkeyImys import usabot

if __name__ == '__main__':
    koto = usabot.Usabot()
    
    koto.circle()

    for i in range(0, 12):
        koto.tap('quest3', 1)
        koto.circle()
    
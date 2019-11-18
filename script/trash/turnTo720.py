k = { 'again':  (1020, 1000),
      'next' :  (1700, 1000), 
      'start':  (1500, 1000),
      #add y 150
      'quest1': (300, 200),
      'quest2': (300, 350),
      'quest3': (300, 500),
      'quest4': (300, 650),
      'quest5': (300, 800),
      #auto click quest 2
      'questAuto':(300, 350),
      'stage':  (1170, 830),
      'close-c':( 950,  800),#first clear
      'close-u':( 950,  770),#lv up
      '1-1:':    (   0,    0),
      'back':    ( 100,   60),
      'HOME':    ( 100, 1000),
      'blank_title':(960, 65),
      'left_switch':(220,1000),
      'right_switch':(1100,990)
}

for item in k.items():
    print('\''+ str(item[0]) +'\''+':'+'('+ str(int(item[1][0]*0.6666)) + ', ' + str(int(item[1][1]*0.6666)) +')'+',')
# fix ImportError: No module named monkeyImys
# add monkeyImys to sys.path
# Run 'monkeyrunner register.py'

# import sys
# from os.path import abspath, join, dirname
# sys.path.insert(0, join(abspath(dirname(__file__)), 'script').encode('ascii'))

# from __future__ import with_statement
# from pathlib import Path
# to_add=Path(join(abspath(dirname(__file__)), 'script').encode('ascii'))
# from sys import path

# if str(to_add) not in path:
#     minLen=999999
#     for index,directory in enumerate(path):
#         if 'site-packages' in directory and len(directory)<=minLen:
#             minLen=len(directory)
#             stpi=index

#     pathSitePckgs=Path(path[stpi])
#     with open(str(pathSitePckgs/'current_machine_paths.pth'),'w') as pth_file:
#         pth_file.write(str(to_add))

# print('register to path!')
print(sys.path)
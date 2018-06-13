import os
import sys

from time import sleep


print('test __file__', __file__)
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.readcsv import readresult


def testresult():
    # while True:
    readresult()
    sleep(5)
    print('.....')


# sys.path.append('../')  # 添加上级目录为模块搜索路径
if __name__ == '__main__':
    print('tests cwd', os.getcwd())
    print(os.path.abspath(__file__))

    print('modified tests cwd', os.getcwd())
    print(os.path.abspath(__file__))
    print('mo tes', sys.path)

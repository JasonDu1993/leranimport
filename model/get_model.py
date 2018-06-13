import os
import sys

print('get_model', sys.path)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
print('modi get_model', sys.path)
from tools.readcsv import readresult


def getmodel():
    # dir_abs_name = os.path.dirname(os.path.abspath(__file__))  # 获取绝对路径下的文件目录
    # print('get model dir_abs_name', dir_abs_name)
    readresult()
    print('diaoyong readcsv', sys.path)

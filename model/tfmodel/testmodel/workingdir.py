import os
import sys

print('workingdir sys.path 1', sys.path)
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
print('workingdir sys.path 2', sys.path)
# from model.get_model import getmodel
print('workingdir __file__', __file__)
from tests.test import testresult
testresult()
# getmodel()
# print('diaoyong getmodel', sys.path)
# dir_abs_name = os.path.dirname(os.path.abspath(__file__))  # 获取绝对路径下的文件目录
# print('dir_abs_name', dir_abs_name)
#
# parent_path = os.path.dirname(dir_abs_name)  # 获得文件的上级目录
# print('parent_path', parent_path)
# parent2_path = os.path.dirname(parent_path)  # 文件的上上级目录
# print('parent2_path', parent2_path)

#
# ch_dir_parent = os.chdir(parent_path)
# print('ch_dir_parent', ch_dir_parent)
#

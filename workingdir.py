import os
import sys


print('sys.path', sys.path)
sys.path.append('..')  # 添加上级目录为模块搜索路径
sys.path.append('../..')  # 添加上上级目录为模块搜索路径
print('modified sys.path', sys.path)

# getmodel()
dir_abs_name = os.path.dirname(os.path.abspath(__file__))  # 获取绝对路径下的文件目录
print('dir_abs_name', dir_abs_name)

parent_path = os.path.dirname(dir_abs_name)  # 获得文件的上级目录
print('parent_path', parent_path)
parent2_path = os.path.dirname(parent_path)  # 文件的上上级目录
print('parent2_path', parent2_path)

#
# ch_dir_parent = os.chdir(parent_path)
# print('ch_dir_parent', ch_dir_parent)
#









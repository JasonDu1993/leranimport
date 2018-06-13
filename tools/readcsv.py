import csv
import os
import sys

print('readcsv __file__', __file__)
print('read sys.path', sys.path)
# sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('..')
print('mo resd sys.path', sys.path)


def readresult(path=None):
    """

    Args:
        path: A str, path of csv file, if is None, set path to result.csv

    Returns:

    """
    # print(os.path.abspath(__file__))
    # print('readcsv cwd', os.getcwd())
    # if path is None:
    #     path = 'result.csv'
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print('change working dir', os.getcwd())
    # print(os.path.abspath(__file__))
    # with open(path, 'r', newline='') as f:
    #     reader = csv.reader(f)
    #     for v in reader:
    #         print(v)

    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result.csv')
    print('sss')
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        line = [1, 2, 3]
        writer.writerow(line)
        # with open(path, 'r', newline='') as f:
        # reader = csv.reader(f)
        # for v in reader:
        #     print(v)

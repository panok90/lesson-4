"""Реализовать два небольших скрипта:
б) итератор, повторяющий элементы некоторого списка, определенного заранее"""


from argparse import ArgumentParser
from itertools import cycle

parser = ArgumentParser()
parser.add_argument('-n', '--number', type=int, default=1)

args = parser.parse_args()

source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

index = 0
for item in cycle(source_list):
    if index > args.number:
        break
    print(item)
    index += 1

"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного"""


from argparse import ArgumentParser
from itertools import count

parser = ArgumentParser()
parser.add_argument('-s', '--start', type=int, default=1)
parser.add_argument('-e', '--end', type=int, default=100)

args = parser.parse_args()

for item in count(args.start):
    if item <= args.end:
        print(item)
    else:
        break

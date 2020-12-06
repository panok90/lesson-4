"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from argparse import ArgumentParser


def payroll_func(val1, val2, val3):
    print(val1 * val2 + val3)


parser = ArgumentParser()
parser.add_argument('-o', '--output', type=int)
parser.add_argument('-r', '--rate', type=float)
parser.add_argument('-p', '--prize', type=float)

args = parser.parse_args()

payroll_func(args.output, args.rate, args.prize)

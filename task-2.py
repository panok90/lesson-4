"""Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента."""

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [val for i, val in enumerate(source_list) if i != 0 and val > source_list[i-1]]
print(result)

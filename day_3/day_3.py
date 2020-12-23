from itertools import product
from pprint import pprint

from functools import reduce

def check_coords(x, y, data, tree_char = "#"):
    if data[y][x] == tree_char:
        return 1
    return 0

tree_data = []
with open('day_3/input') as reader:
    for line in reader:
        tree_data.append(line.strip())

# pprint(tree_data)

def check_data_slope(slope_x, slope_y, data):
    x, y = 0, 0
    tree_count = 0
    x_wrap = len(data[0])

    while y < len(data):
        print(f"coords: {x}, {y}")
        print(f"coord val: {data[y][x]}")
        tree_count += check_coords(x, y, data)

        y += slope_y
        temp_x = (x + slope_x) % x_wrap
        x = temp_x

    return tree_count
    

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]
results = [check_data_slope(s_x, s_y, tree_data) for s_x, s_y in slopes]
print(results)
print(reduce( (lambda x, y: x * y), results))
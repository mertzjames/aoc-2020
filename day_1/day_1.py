from itertools import permutations

with open('day_1/input') as reader:
    data = [int(x) for x in reader]

# part 1
combos = permutations(data, 2)
for a, b in combos:
    if a + b == 2020:
        print(a * b)

# part 2
combos = permutations(data, 3)
for a, b, c in combos:
    if a + b + c == 2020:
        print(a * b * c)
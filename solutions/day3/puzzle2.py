import re
from string import punctuation

data = open("input.txt").read().strip()

nums = []
symbols = set()
re_syms = "|".join(re.escape(s) for s in punctuation if s != ".")
width = len(data.split("\n")[0])
height = len(data.split("\n"))

for i, line in enumerate(data.split("\n")):
    for j in re.finditer(r"\d+", line):
        nums.append((j.group(), i, j.start()))
    for j in re.finditer(re_syms, line):
        symbols.add((i, j.start()))


def coverage(num, row, col):
    return [
        (y, x)
        for y in range(row - 1, row + 2)
        for x in range(col - 1, col + len(num) + 1)
        if 0 <= y <= width and 0 <= x <= height
    ]

res = 0
for s in symbols:
    matching_nums = set()
    for n in nums:
        num, row, col = n
        if s in coverage(*n):
            matching_nums.add(int(num))
        if len(matching_nums) == 2:
            product = 1
            for num in matching_nums:
                product *= num
            res += product
            break
print(res)
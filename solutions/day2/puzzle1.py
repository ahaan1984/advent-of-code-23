import re

instances = {'red': 12, 'blue': 14, 'green': 13}

total = 0
for x, line in enumerate(open("input.txt")):
    exp = re.findall(r'(\d+) (red|blue|green)', line)
    if any(int(pull[0]) > instances[pull[1]] for pull in exp):
        total += x + 1
print(total)
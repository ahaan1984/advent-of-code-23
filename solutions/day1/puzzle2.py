number_table = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

sol = []

with open("input.txt") as f:
    f = f.read().strip()
    for k, v in number_table.items():
        f = f.replace(k, v)
    for line in f.split("\n"):
        nums = ''.join([char for char in line if char.isdigit()])
        sol.append(int(nums[0]+nums[-1]))
print(sum(sol))
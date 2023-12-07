sol = []
with open('input.txt') as f:
    for input in f.readlines():
        nums = ''.join([i for i in input if i.isdigit()])
        sol.append(int(nums[0] + nums[-1]))    
print(sum(sol))

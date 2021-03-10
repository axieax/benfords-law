import re

# input expenses
with open('andrew.txt') as f:
    nums = re.findall(r'\d+\.?\d*', f.read())
    assert len(nums) == 50

# compute frequency
d = {str(x): 0 for x in range(10)}
for num in nums:
    d[num[0]] += 1

# compute percentage
for digit, freq in d.items():
    print(f'{digit}: {freq / len(nums) * 100}%')

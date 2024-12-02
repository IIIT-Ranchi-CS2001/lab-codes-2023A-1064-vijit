nums = [int(x) for x in input("Enter space-separated integers: ").split()]

mean = sum(nums) / len(nums)

nums.sort()
n = len(nums)
if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

max_count = max(freq.values())
modes = [k for k, v in freq.items() if v == max_count]

if len(modes) == 1:
    mode = modes[0]
else:
    mode = modes  

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

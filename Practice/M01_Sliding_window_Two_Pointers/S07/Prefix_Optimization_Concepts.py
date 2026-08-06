#1480 Running Sum of 1d Array
'''
nums = [1, 2, 3, 4]
res = [0] * len(nums)
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i + 1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)'''
# 1732 Find the Highest Altitude
n = 5
gain = [-5, 1, 5, 0, -7]
altitudes = [0] * (n + 1)
for i in range(n):
    altitudes[i + 1] = altitudes[i] + gain[i]
print(max(altitudes))
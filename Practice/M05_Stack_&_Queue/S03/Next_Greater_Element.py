#496 Next Greater Element I
#https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    d = {}
    n = len(nums2)
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        if not stack:
            d[nums2[i]] = -1
        else:
            d[nums2[i]] = stack[-1]
        stack.append(nums2[i])
    res = []
    for ele in nums1:
        res.append(d[ele])
    return res
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
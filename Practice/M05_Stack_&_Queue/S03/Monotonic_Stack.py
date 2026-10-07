'''#1. Monotonic Increasing Stack
#General pattern
arr = [4,12,5,3,1,2,5,3,1,2,6,4]
stack = []
for x in arr:
    while stack and stack[-1] > x:
        stack.pop()
    stack.append(x)

#2. Monotonic Decreasing Stack
#General pattern
stack = []
for x in arr:
    while stack and stack[-1] < x:
        stack.pop()
    stack.append(x)

#Next Greater Element
def NextGreaterElement(arr):
    n = len(arr)
    res = [0] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return res
arr = [4,12,5,3,1,2,5,3,1,2,6,4]
#output = [12,-1,6,5,2,5,6,4,2,4,6,-1]
print(NextGreaterElement(arr))
'''
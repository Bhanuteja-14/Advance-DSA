'''
input:[12,45,63,20,96,25,10]
output:[12,20,96,10]
create an empty list
traverse the array and check element is even or odd
if element is even then add it to res
display the res
'''
'''arr = list(map(int,input().split()))
res = []
for i in arr:
    if i%2==0:
        res.append(i)
print(res)



solve the problem using two pointer technique
'''
arr = list(map(int,input().split()))
i = 0
for j in range(len(arr)):
    if arr[j]%2==0:
        arr[i] = arr[j]
        i+=1
print(arr[:i])
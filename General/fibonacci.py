# Print numbers in fibonacci sequence
'''
print("enter a number to find the fibonacci of")
num = int(input())
v1 = 0
v2 = 1
temp = 0
for x in range (0, num):
    #print(x)
    print (v1)
    temp = v1 + v2
    v1 = v2
    v2 = temp 
'''

print("enter a number to find the fibonacci of")
num = int(input())
v1 = 0
v2 = 1
temp = 0
while v1 <= num :
    #print(x)
    print (v1)
    temp = v1 + v2
    v1 = v2
    v2 = temp 

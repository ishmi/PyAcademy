# Print foo is multiple of 3, bar if multiple of 5 and foobar if multiple of 15
print("how far do you want to go?")
num = int(input())
for j in range (1, num + 1):
    if j % 3 == 0:
        if j % 5 == 0:
            print("foobar")
        else:
            print("foo")
    else:
        if j % 5 == 0:
            print("bar")
        else:
            print(j)
    
    

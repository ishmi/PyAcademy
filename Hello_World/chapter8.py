'''
#problem number 1 (for-loop)
print ("Which multiplication table would you like?")
a = int(input())
for j in range(0, 11):
    print (a, "x", j, "=", j*a)
   
#problem number 2 (while-loop)
print "Which multiplication table would you like?"
a = int(raw_input())
j = 1
while j < 11 :
    print (a, "x", j, "=", j*a)
    j = j+1
    
# problem number 3
print "Which multiplication table would you like?"
a = int(raw_input())
print "how high would you like the mutiplication table to go?"
n = int(raw_input())
for j in range(0, n+1):
    print (a, "x", j, "=", j*a)
'''

print ("How much should we count by?")
c = int(input())
for b in range(0, 100, c) :
    print("********", b)

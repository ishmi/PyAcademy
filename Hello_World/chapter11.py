'''numLines = int(input('How many lines of stars do you want? '))
numStars = int(input('How many stars per line? '))
for line in range(0, numLines):
    for star in range(0, numStars):
        print('* ', end='')
    print()'''

#Problem number 1
print ("Countdown timer; how many seconds would you like?")
time = input()
while time > 0:
    print(time)
    time = time - 1
if time == 0 :
    print("BLAST OFF!")

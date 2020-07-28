'''
# Problem number 1
print "What is the original purchase price?"
price = float(raw_input())
if price <= 10 :
    print ("you get a 10% discount, the final price is", price*0.9, "US dollars")
else :
    print ("you get a 20% discount, the final price is", price*0.8, "US dollars")
'''
# Problem number 2
print "A local soccer team is trying to recruit members. Are you eligible?"
print " Please indicate your gender {m , f}"
gender = str(raw_input())
if gender == 'm' :
    print "sorry, you are not eligible for this team."
else :
    print "what is your age?"
    age = int(raw_input())
    if 10 <= age <= 12 :
         print " you are eligible for this team"
    else :
         print "sorry, you cannot participate in the team"

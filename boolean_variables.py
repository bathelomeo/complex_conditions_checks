# I check to see if the requirements for honour rol are met
gpa = int(input('What was your Grade Point Average? '))
lowest_Grade = int(input('What was your lowest Grade? '))

if gpa >= 85 and lowest_Grade >= 70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code if you need to check if students is
# on honour roll, all i need to do is check the boolean variable
# I set earlyer in my code
if honour_roll:
    print ('You made the honour roll')

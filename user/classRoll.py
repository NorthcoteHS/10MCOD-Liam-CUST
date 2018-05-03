roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Micheal', 'Everett', 'Lisa', 'Sam', 'Noah']
print ('turn to cleanin guinea pig cage: ', roll[2])

enrolment = len(roll)
roll.append('James')
del roll[2]
roll[4] = 'Mike'
print('Class roll:')
print(roll)
rollalpha = [roll[-7], roll[-9], roll[-5], roll[-1], roll[-10], roll[-8], roll[-4], roll[-6], roll[-2], roll[-3] ]
print('Alphbetic roll order:')
print(rollalpha)
list.reverse(rollalpha)
print('Reversed roll: ')
print(rollalpha)
from random import randint
number = (randint(1, 10))
if number == 1:
    print(rollalpha[0])
if number == 2:
    print(rollalpha[1])
if number == 3:
    print(rollalpha[2])
if number == 4:
    print(rollalpha[3])
if number == 5:
    print(rollalpha[4])

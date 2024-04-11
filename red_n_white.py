'''
      Condition : 1. if Red on 1st row is Present and White at 3rd row be calam
                  2. if one is absent talk with other
                  3. if condition 1 is false -> Talk with green
      '''

import random

RED ='Red'
WHITE = 'White'
GREEN ='Green'

colors = [RED, 'Blue', GREEN, 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', WHITE, 
          'Gray', 'Gold', 'Silver', 'Maroon', 'Navy']
random.shuffle(colors)

'''
#make a list of 3 in mega list of seating list -> [[0,0,0], [0,0,0], [0,0,0]]
seating_arrangements =[[0]*3 for _ in range(4)]
'''

# It will pop from colors list and returnd the First element
seating_arrangements = [[colors.pop(0) for _ in range(3)] for _ in range(4)]

'''
#the above line will replace the below block
color_index = 0
for row in range(4): # each rows 
    for seat in range(3):# each column
        seating_arrangements[row][seat] = colors[color_index]
        color_index += 1
'''

# alert_for_red = False
# alert_for_white = False
# alert_for_green = False

# #directly given condition 
alert_for_red = RED in seating_arrangements[0]
alert_for_white = WHITE in seating_arrangements[2]
alert_for_green = any(GREEN in row for row in seating_arrangements)

print('''
      Condition : 1. if Red on 1st row is Present and White at 3rd row be calam
                  2. if one is absent talk with other
                  3. if condition 1 is false -> Talk with green
      ''')
for row in range(3):
    print(seating_arrangements[row])
    # if(RED in seating_arrangements[0]): alert_for_red = True
    # if (WHITE in seating_arrangements[2]): alert_for_white = True
    if (GREEN in seating_arrangements[row]): 
        alert_for_green = True 
        post = row


if(alert_for_red and alert_for_white): print('Alert! Stay calmn')
elif(alert_for_white): print('Hayee to White sitting at row 3')
elif(alert_for_red): print('Hayee to Red at row 1')
if(alert_for_green): print(f'Hayee to Green seating at row {post+1}')
else: print(f'Move on')
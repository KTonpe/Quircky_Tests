'''
4 lists = 4 rows
random seats blocked
2nd red and 4th white check on 2nd seat only stay calm
if one is missing say haayeee to another
if both are absent move on and hayee to green
'''


import random

RED ='Red'
WHITE = 'White'
GREEN ='Green'

colors = [RED, 'Blue', GREEN, 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', WHITE, 
          'Gray', 'Gold', 'Silver', 'Maroon', 'Navy']
random.shuffle(colors)

#make a list of 3 in mega list of seating list -> [[0,0,0], [0,0,0], [0,0,0]]
seating_arrangments =[[0]*3 for _ in range(1,5)]
color_index = 0
for row in range(4): # each rows 
    for seat in range(3):# each column
        seating_arrangments[row][seat] = colors[color_index]
        color_index += 1

alert_for_red = False
alert_for_white = False
alert_for_green = False
print('''
      Condition : 1. if Red on 1st row is Present and White at 3rd row be calam
                  2. if one is absent talk with other
                  3. if condition 1 is false -> Talk with green
      ''')
for row in range(3):
    print(seating_arrangments[row])
    if(RED in seating_arrangments[0]): alert_for_red = True
    if (WHITE in seating_arrangments[2]): alert_for_white = True
    if (GREEN in seating_arrangments[row]): 
        alert_for_green = True 
        post = row


if(alert_for_red == True and alert_for_white == True): print('Alert! Stay calmn')
if(alert_for_red == False and alert_for_white == True): print('Hayee to White sitting at row 3')
if(alert_for_white == False and alert_for_red == True): print('Hayee to Red at row 1')
if(alert_for_red == False and alert_for_white == False and alert_for_green == True): print(f'Hayee to Green seating at row {post+1}')
if(alert_for_red == False and alert_for_white == False and alert_for_green == False): print(f'Move on')
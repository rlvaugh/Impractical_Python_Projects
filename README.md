# Impractical_Python_Projects

Errata From https://nostarch.com/impracticalpythonprojects

Page 79: code output at bottom of page is based on Figure 4-3, not Figure 4-2.

Page 85: In Listing 4-9, the code at wingding 5 and the following line that read:
    row1 = (message[:row_1_len])
    row2 = (message[row_1_len:])
Should instead read:
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:]).lower()
    
Also in Listing 4-9, the code immediately below wingding 8 that reads:
        plaintext.append(r1.lower())
        plaintext.append(r2.lower())
Should instead read:
        plaintext.append(r1)
        plaintext.append(r2)
        
Page 100: The output printout near the bottom of page that reads:
Panel at east end of chapel slides
Should instead read:
Panelateastendofchapelslides

Page 103: The cipher example that reads:
The cold tea didn’t please the old finicky woman.
Should instead read:
So, the cold tea didn’t please the old finicky woman.

Page 141: Wingding 7 and the preceding line in Listing 7-10 that read:
lock_wheel = int(randrange(0, len(combo)))
next_try[lock_wheel] = randint(0, len(combo)-1)
Should instead read:
lock_wheel = randrange(0, len(combo))
next_try[lock_wheel] = randint(0, 9)

Page 205: The line and following equation that read:
The transformation to generate points over a unit disc is as follows:
x= √r*cos
Should instead read as:
The transformation to generate points evenly over a unit disc is:
x= √r*cosθ

And the line that reads:
The equations yield (x, y) values between 0 and 1.
Should instead read as:
The equations yield (x, y) values between -1 and 1.

Page 218: Indentation for the listing on the page should be as follows:
>>> from random import randint

>>> trials = 100000

>>> success = 0

>>> for trial in range(trials):

           faces = set()
           
           for rolls in range(6):
           
               roll = randint(1, 6)
               
               faces.add(roll)
               
           if len(faces) == 6:
           
               success += 1
               
>>> print("probability of success = {}".format(success/trials))
probability of success = 0.01528

Page 250: Listing 12-1 should read as:
import sys
import random
import matplotlib.pyplot as plt
 
def read_to_list(file_name):   
    """Open a file of data in percent, convert to decimal & return a list."""
    with open(file_name) as in_file: 
        lines = [float(line.strip()) for line in in_file] 
        decimal = [round(line / 100, 5) for line in lines]
        return decimal
 
def default_input(prompt, default=None):    
    """Allow use of default values in input"""
    prompt = '{} [{}]: '.format(prompt, default)
    response = input(prompt)
    if not response and default:        
        return default    
    else:        
        return response
        
Page 252: The last line on page that reads:
Set the default to 'sbc_blend', since this is theoretically the most stable mix of the four choices.
Should instead read as:
Set the default to 'bonds', in order to see how this supposedly “safe” choice performs.

Page 259: The first line in last paragraph that reads:
Let’s work an example that assumes a starting value of $2,000,000, a “safe and secure” bond portfolio, a 4 percent withdrawal rate (equal to $80,000 per year), a 30-year retirement, and 50,000 cases.
Should instead read as:
Let’s work an example that assumes a starting value of $2,000,000, a “safe and secure” bond portfolio, a 4 percent withdrawal rate (equal to $80,000 per year), a 29-30-31 retirement range, and 50,000 cases.

Page 261: The last two lines in Listing 12-9 that read:
    investments -= withdraw_infl_adj
          investments = int(investments * (1 + i))          
Should instead read as:
            investments -= withdraw_infl_adj
            investments = int(investments * (1 + i)) 
            
Page 305: In the last paragraph, transform_rotate() should be transform.rotate()

Page 356: Between wingdings 5 and 6, Listing 16-2 should read as:
    # check for missing digits
    keys = [str(digit) for digit in range(1, 10)]
    for key in keys:
        if key not in first_digits:
            first_digits[key] = 0  
            
Page 368: The code for Dictionary Cleanup should read as:
"""Remove single-letter words from list if not 'a' or 'i'."""
word_list = ['a', 'nurses', 'i', 'stack', 'b', 'c', 'cat']
word_list_clean = []
 
permissible = ('a', 'i')
 
# remove single-letter words if not "a" or "I"
for word in word_list:
    if len(word) > 1:
        word_list_clean.append(word)
    elif len(word) == 1 and word in permissible:
        word_list_clean.append(word)
    else:
        continue 
print("{}".

from pyfiglet import Figlet

figlet = Figlet()

import sys

import random

#check if user provides correct number of arguments
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit('Invalid usage')
#check for the case of two arguments
elif len(sys.argv) == 3:
    if sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit('Invalid usage')

print('Output: ')
if len(sys.argv) == 1:
#get input from user
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)
    print(figlet.renderText(text))
else:
    text = input('Input: ')
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(text))

import sys
#from PIL lib import two modules
from PIL import Image, ImageOps
#import os module
import os

def main():
    check_arg()
    create_pic()

def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    extensions = ('.jpeg','.png','jpg')
    if sys.argv[1].endswith(extensions) and sys.argv[2].endswith(extensions):
        if not os.path.splitext(sys.argv[1])[1] == os.path.splitext(sys.argv[2])[1]:
            sys.exit('Input and output have different extensions')
    else:
        sys.exit('Invalid output')

def create_pic():
    try:
        #both Image and ImageOps are modules in PIL lib
        #use open fucntion from Image module to open shirt and input pic
        shirt = Image.open('shirt.png')
        photo = Image.open(sys.argv[1])
        #use size to get size of shirt
        size = shirt.size
        #use fit function from ImageOps module to crop input pic
        photo = ImageOps.fit(photo, size)
        #overlay shirt on input pic
        photo.paste(shirt, shirt)
        #save new pic to second command_line argument (save as the filename)
        photo.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit('Input does not exists')


if __name__ == '__main__':
    main()

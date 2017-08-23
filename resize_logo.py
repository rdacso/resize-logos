import os, sys

from PIL import Image, ImageDraw

directory = sys.argv[1]
file = sys.argv[2]
file_content = os.path.join(directory + '/' + file)


def add_white_background(ImageFilePath):

    image = Image.open(ImageFilePath)


    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height

        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        imResize = background.resize((400,400), Image.ANTIALIAS)
        imResize.save('logo.png')

        print "Image has been resized !"
        imResize.show()

    return image


    

add_white_background(file_content)


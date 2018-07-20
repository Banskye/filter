# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename)

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(any_img):
    any_img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(any_img, filename):
    any_img.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(any_img):
    new_img = Image.new("RGB", any_img.size)

    yellow = (252,227,166)

    lightBlue = (112,150,158)

    red = (217,26,33)

    darkBlue = (0,51,76)

    # gather data into a list
    newPixels = []
    # get data/list of pixels from original image
    imagePixels = list(any_img.getdata())

    for individualPixel in imagePixels:
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue

        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182:
            newPixels.append(red)
        elif intensity < 546 and intensity >=364:
            newPixels.append(lightBlue)
        else:
            newPixels.append(yellow)

    new_img.putdata(newPixels)

    return new_img

def viv(any_img):
    new_img = Image.new("RGB", any_img.size)

    green = (209,234,153)

    lightBlue = (53,167,176)

    blue = (9,72,113)

    darkBlue = (0,51,76)

    # gather data into a list
    newPixels = []
    # get data/list of pixels from original image
    imagePixels = list(any_img.getdata())

    for individualPixel in imagePixels:
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue

        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182:
            newPixels.append(blue)
        elif intensity < 546 and intensity >=364:
            newPixels.append(lightBlue)
        else:
            newPixels.append(green)

    new_img.putdata(newPixels)

    return new_img

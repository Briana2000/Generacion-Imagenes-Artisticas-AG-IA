import cv2
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from math import ceil

# constants
SQUARE_SIZE = 100

def preprocessing():
    # read the image
    image = cv2.imread('./img/image.jpg')

    # convert to rgb schema in case it is bgr
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # add some extra pixels to the image to make it divisible by squares of pixels with SQUARE_SIZE
    
    height, width, _ = image.shape # get height and width of the original image.

    """ 
    This line calculates how many additional pixels must be added in the height direction 
    so that the total height is divisible by SQUARE_SIZE. Ceil rounds up dividing the current 
    height by SQUARE_SIZE. It is then multiplied again by SQUARE_SIZE to get the adjusted 
    height and subtracted from the original height to get the number of pixels to add.
    """
    height_offset = ceil(height / SQUARE_SIZE) * SQUARE_SIZE - height

    # As same as with height we calculate ho many pixels to add to the width to make it divisible by SQUARE SIZE
    width_offset = ceil(width / SQUARE_SIZE) * SQUARE_SIZE - width

    """ 
    With cv2.copyMakeBorder we add the extra pixels to the borders of the image. 
    And with cv2.BORDER_REFLECT we specifies the fill method to use. In this case, the reflection 
    method is used, which means that the pixels will be reflected along the edges, creating a mirror 
    effect.
    """
    image = cv2.copyMakeBorder(image, 0, height_offset, 0, width_offset, cv2.BORDER_REFLECT)
    height, width, _ = image.shape

    # new image
    im = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(im)

   # Draw the squares in the image
    for y in range(0, height, SQUARE_SIZE):
        for x in range(0, width, SQUARE_SIZE):
            draw.rectangle([x, y, x + SQUARE_SIZE, y + SQUARE_SIZE], outline='white')

    # convert the image from OpenCV to RGB format 
    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    im.paste(Image.fromarray(image_rgb), (0, 0))

    # show the generated image
    plt.imshow(im)
    plt.show()

    # save the image
    im.save('./img/result.png')     


if __name__ == "__main__":
  preprocessing()


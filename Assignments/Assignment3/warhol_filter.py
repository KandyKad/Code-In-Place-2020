"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    image = SimpleImage(PATCH_NAME)
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    patch = make_recolored_patch(1.5, 0, 1.5)  # 1

    for x in range(int(WIDTH/3)):
        for y in range(int(HEIGHT/2)):
            pixel = patch.get_pixel(x,y)
            final_image.set_pixel(x, y, pixel)

    aatch = make_recolored_patch(0, 1.5, 1.5)  # 2

    for x in range(int(WIDTH/3)):
        for y in range(int(HEIGHT/2)):
            pixel = aatch.get_pixel(x,y)
            final_image.set_pixel(WIDTH*1/3 + x, y, pixel)

    batch = make_recolored_patch(1.5, 1.5, 1.5)  # 3

    for x in range(int(WIDTH/3)):
        for y in range(int(HEIGHT/2)):
            pixel = batch.get_pixel(x,y)
            final_image.set_pixel(WIDTH*2/3 + x, y, pixel)

    catch = make_recolored_patch(1.5, 1.5, 0)  # 4

    for x in range(int(WIDTH/3)):
        for y in range(int(HEIGHT/2)):
            pixel = catch.get_pixel(x,y)
            final_image.set_pixel(x, HEIGHT/2 + y, pixel)

    datch = make_recolored_patch(1, 1, 1)  # 5

    for x in range(int(WIDTH/3)):
        for y in range(int(HEIGHT/2)):
            pixel = datch.get_pixel(x,y)
            final_image.set_pixel(WIDTH*1/3 + x, HEIGHT/2 + y, pixel)

    eatch = make_recolored_patch(1, 1, 4.5)
    for x in range(int(WIDTH/3)):
        for y in range(int(HEIGHT/2)):
            pixel = eatch.get_pixel(x,y)
            final_image.set_pixel(WIDTH*2/3 + x, HEIGHT/2 + y, pixel)

    # This is an example which should generate a pinkish patch

    #patch = make_recolored_patch(1.5, 0, 1.5)  #1
    #batch = make_recolored_patch(1.5, 1.5, 0)  #4
    #catch = make_recolored_patch(0, 0, 1.5)  #6
    #datch = make_recolored_patch(1.5, 0, 0)
    #eatch = make_recolored_patch(0, 1.5, 0)
    #fatch = make_recolored_patch(0.5, 0.5, 1.5)  #3


    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)

    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale

    return patch

if __name__ == '__main__':
    main()
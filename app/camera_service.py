import imageio
import imageio as iio
import matplotlib.pyplot as plt
from matplotlib import image as mpimg


def take_photo():
    # camera = iio.get_reader("<video8>")
    # screenshot = camera.get_data(0)
    # camera.close()
    # imageio.imwrite("/tmp/test.jpg", screenshot)
    #
    plt.clf()
    img = mpimg.imread('IMG.jpg')
    # Display the image
    plt.imshow(img)
    plt.show(block=False)



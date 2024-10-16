import threading

import matplotlib.pyplot as plt
from matplotlib import image as mpimg


def take_photo():
    t = threading.Thread(target=show)
    t.setDaemon(True)
    t.start()


def show():
    plt.clf()
    img = mpimg.imread('IMG.jpg')
    # Display the image
    plt.imshow(img)
    plt.show(block=False)



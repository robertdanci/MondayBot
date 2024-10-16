import imageio as iio
import matplotlib.pyplot as plt

def take_photo():
    camera = iio.get_reader("<video8>")
    screenshot = camera.get_data(0)
    camera.close()

    plt.imshow(screenshot)



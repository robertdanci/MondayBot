import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

def take_photo():
    cam = pygame.camera.Camera('/dev/video8')
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, "/tmp/captured_image.jpg")
    cam.stop()



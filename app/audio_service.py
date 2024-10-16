import pygame

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("403057__vesperia94__hooray.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
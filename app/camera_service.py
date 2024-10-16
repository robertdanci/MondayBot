import subprocess


def take_photo():
    subprocess.check_output(["open ~/MondayBot/IMG.jpg &"], shell=True)



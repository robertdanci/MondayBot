from pydub import AudioSegment
from pydub.playback import play


def play_audio():
    song = AudioSegment.from_wav("403057__vesperia94__hooray.wav")
    play(song)
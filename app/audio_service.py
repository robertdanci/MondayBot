from pydub import AudioSegment

def play_audio():
    song = AudioSegment.from_wav("403057__vesperia94__hooray.wav")
    song.play()
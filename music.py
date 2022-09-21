import os

class Music:
    # play sound
    def play_music(self):
        file = "music/LoodiMusic.wav"
        os.system("afplay " + file)
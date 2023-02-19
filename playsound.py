import vlc
import time

p = vlc.MediaPlayer("sirine.mp3")
p.play()
time.sleep(10)
p.stop()
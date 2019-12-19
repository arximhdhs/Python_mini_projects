import requests
import os
import sys
from pydub import AudioSegment
from pydub.playback import play
# dirName = '/home/kouts/Documents/operations/hulio/'
 

# os.mkdir(dirName)


dir_name = '/home/kouts/Documents/books/'
mp3_name = dir_name + '1984/'+'1984-1.mp3' 
new_dir = '/home/kouts/Documents/books/tester/test.mp3'
print(mp3_name)
song = AudioSegment.from_mp3(mp3_name)
print(song.dBFS)
louder_song = song - 15
print(louder_song.dBFS)
louder_song.export(new_dir , format='mp3')

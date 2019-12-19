
import requests
import os
import sys
from pydub import AudioSegment
from pydub.playback import play
# dirName = '/home/kouts/Documents/operations/hulio/'
 

# os.mkdir(dirName)

book_name = sys.argv[1]
how_many = int(sys.argv[2])
num = int(sys.argv[3])
print(book_name)

dir_name = '/home/kouts/Documents/books/' + book_name ;
os.mkdir(dir_name)
for i in range(how_many):
    url = 'http://www.isobitis.com/audio%20books/books' + '0'+ str((num+i)) + '.mp3'
    print(url)
    mp3_name = dir_name + '/' + book_name + '-' + str(i+1) + '.mp3'
    print(mp3_name)
    r = requests.get(url, allow_redirects=True)
    open(mp3_name, 'wb').write(r.content)
    song = AudioSegment.from_mp3(mp3_name)
    print(song.dBFS)
    value = -song.dBFS - 15
    louder_song = song  + value
    print(louder_song.dBFS)
    louder_song.export(mp3_name, format='mp3')


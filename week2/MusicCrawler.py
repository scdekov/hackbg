from playlist import Playlist
from song import Song
import glob
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3



class MusicCrawler():

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        playlist = Playlist("newList")
        os.chdir(self.path)
        for songa in glob.glob("*.mp3"):
            song = MP3(songa, ID3=EasyID3)
            try:
                playlist.add_song(Song(song.tags["title"][0], song.tags["artist"][0], "", 0, song.info.length, song.info.bitrate))
            except TypeError:
                pass
            except KeyError:
                pass
        print (playlist)


def main():
    #music = MusicCrawler("/home/svetlio/Documents/programming101/week2")
    music = MusicCrawler("/home/svetlio/Music")
    music.generate_playlist()


if __name__ == '__main__':
    main()

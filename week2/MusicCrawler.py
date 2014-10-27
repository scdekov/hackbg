from playlist import Playlist
from song import Song
import glob
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3



class MusicCrawler():

    def __init__(self, path):
        playlist = Playlist("newList")
        os.chdir(path)
        for song in glob.glob("*.mp3"):
            song = MP3(song, ID3=EasyID3)
            playlist.add_song(Song(song.tags["title"][0], song.tags["artist"][0], "", 0, song.info.length, song.info.bitrate), )

        print (playlist)


def main():
    music = MusicCrawler("/home/svetlio/Music")


if __name__ == '__main__':
    main()

import json
from song import Song
from mutagen.mp3 import MP3


class Playlist():

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, title):
        counter = 0
        for song in self.songs:
            if song.title == title:
                counter += 1
        for i in range(counter):
            self.songs.remove(song)

    def total_length(self):
        result = 0
        for song in self.songs:
            result += song.length
        return result

    def remove_disrated(self, minRate):
        for song in self.songs:
            if song.rating < minRate:
                self.remove_song(song.title)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate < 100:
                self.remove_song(song.title)

    def show_artists(self):
        result = set()
        for song in self.songs:
            result.add(song.artist)
        return result

    def __str__(self):
        result = ""
        for song in self.songs:
            result += "{} {} - {}\n".format(song.artist, song.title, "{}:{}".format(song.length // 60, song.length % 60))
        return result

    def save(self, filename):
        file = open(filename, "w+")

        content = []
        for song in self.songs:
            content.append({"title": song.title, "artist": song.artist, "album": song.album, "rating": song.rating, "length": song.length, "bitrate": song.bitrate})
        dic = {"name": self.name, "songs": content}
        file.write(json.dumps(dic))
        file.close()


    def load(self, filename):
        file = open(filename, "r")
        song_info = json.loads(file.read())
        file.close()
        self.name = song_info["name"]
        for song in song_info["songs"]:
            self.add_song(Song(song["title"], song["artist"], song["album"], song["rating"], song["length"], song["bitrate"]))
        file.close()



def main():
    playlist = Playlist("first")
    song = Song("title", "artist", "album", 4, 200, 256)
    beat = Song("beat", "dlg", "hrdlg", 2, 150, 20)
    playlist.add_song(song)
    playlist.add_song(beat)
    playlist.save("file.txt")
    playlist2 = Playlist("second")
    playlist2.load("file.txt")
    print(playlist2)
    audio = MP3("SPENS feat  GOODSLAV   НОВАТА ВЪЛНА [ Official HD Video ].mp3")
    print(audio['TDEN'])







if __name__ == '__main__':
    main()

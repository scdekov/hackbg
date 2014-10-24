from playlist import Playlist
import unittest
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("name")
        self.song = Song("title", "artist", "album", 4, 200, 256)
        self.beat = Song("beat", "dlg", "hrdlg", 2, 150, 20)

    def test_init_playlist(self):
        self.assertEqual(self.playlist.name, "name")
        self.assertEqual(len(self.playlist.songs), 0)

    def test_add_song(self):
        self.playlist.add_song(self.song)
        self.assertEqual(self.playlist.songs[0], self.song)

    def test_remove_song(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song)
        self.playlist.remove_song("title")
        self.assertEqual(len(self.playlist.songs), 0)

    def test_total_length(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.beat)
        self.assertEqual(self.playlist.total_length(), 350)

    def test_remove_disrated(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.beat)
        self.playlist.remove_disrated(3)
        self.assertEqual(len(self.playlist.songs), 1)
        self.playlist.remove_disrated(5)
        self.assertEqual(len(self.playlist.songs), 0)

    def test_remove_bad_quality(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.beat)
        self.playlist.remove_bad_quality()
        self.assertEqual(len(self.playlist.songs), 1)

    def test_show_artists(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.beat)
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.beat)
        result = set()
        result.add("artist")
        result.add("dlg")
        self.assertEqual(self.playlist.show_artists(), result)

    def test_to_str(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.beat)
        result = "artist title - 3:20\ndlg beat - 2:30\n"
        self.assertEqual(str(self.playlist), result)

if __name__ == '__main__':
    unittest.main()




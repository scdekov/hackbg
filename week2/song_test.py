import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("title", "artist", "album", 4, 200, 256)

    def test_song_init(self):
        self.assertEqual(self.song.title, "title")
        self.assertEqual(self.song.artist, "artist")
        self.assertEqual(self.song.album, "album")
        self.assertEqual(self.song.rating, 4)
        self.assertEqual(self.song.length, 200)
        self.assertEqual(self.song.bitrate, 256)

    def test_rate(self):
        self.song.rate(3)
        self.assertEqual(self.song.rating, 3)

    def test_rate_wrong(self):
        with self.assertRaises(ValueError):
            self.song.rate(6)

        with self.assertRaises(ValueError):
            self.song.rate(-1)

if __name__ == '__main__':
    unittest.main()

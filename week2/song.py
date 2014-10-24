

class Song():
    MAX_RATE = 5
    MIN_RATE = 0

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate):
        if self.MIN_RATE < 0 or self.MAX_RATE > 5:
            raise ValueError("Rating must be between {} and {}".format(self.MIN_RATE, self.MAX_RATE))
        else:
            self.rating = rate


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __getitem__(self, index):
        return self.songs[index]

    def __setitem__(self, index, value):
        self.songs[index] = value

    def __len__(self):
        return len(self.songs)

    def __contains__(self, item):
        return item in self.songs


p = Playlist(["song1", "song2", "song3"])

print(p[0])          # song1
print(len(p))        # 3
print("song2" in p)  # True
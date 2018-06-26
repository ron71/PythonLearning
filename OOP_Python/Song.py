class Song:
    """ Class to represent the song
        Attributes:
        title (str)-  The title of the song
        artist (Artist)- The artist of the song
        duration (int) - Duration of the song

    """

    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration


help(Song)
# O/P:
# class Song(builtins.object)
#     |  Class to represent the song
#     |  Attributes:
#     |  title (str)-  The title of the song
#     |  artist (Artist)- The artist of the song
#     |  duration (int) - Duration of the song
#     |
#     |  Methods defined here:
#     |
#     |  __init__(self, title, artist, duration=0)
#     |      :param title: initializes title of the song
#     |      :param artist: initializes artist of the song
#     |      :param duration: initializes duration of the song, zero by default if not initialized
#     |
#     |  ----------------------------------------------------------------------
#     |  Data descriptors defined here:
#     |
#     |  __dict__
#     |      dictionary for instance variables (if defined)
#     |
#     |  __weakref__
#     |      list of weak references to the object (if defined)


# We can also add docString in following way:
Song.__init__.__doc__ = """

        :param title: initializes title of the song
        :param artist: initializes artist of the song
        :param duration: initializes duration of the song, zero by default if not initialized
        """
help(Song.__init__)
# O/P:
# Help on function __init__ in module __main__:
#
# __init__(self, title, artist, duration=0)
# :param title: initializes title of the song
# :param artist: initializes artist of the song
# :param duration: initializes duration of the song, zero by default if not initialized

print(Song.__doc__)
# O/P:
# Class to represent the song
#       Attributes:
#       title (str)-  The title of the song
#       artist (Artist)- The artist of the song
#       duration (int) - Duration of the song

print(Song.__init__.__doc__)
# O/P:
#       :param title: initializes title of the song
#       :param artist: initializes artist of the song
#       :param duration: initializes duration of the song, zero by default if not initialized


class Album:
    """ Class to represent album using it's track lists.

    Attributes:
        name (str) : The name of the album
        year (int): the year of the album released.
        artist (Artist): The artist responsible for the album.
            if not specified, the artist will default to an artist wit name "Various Artists"
        track (List[Song]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.track = list()

    def add_song(self, song, position=None):
        """
        Adds the song in the track list.
        Args:
            :param song: (Song) A song to add.
            :param position: (Optional[int]): if specified song will be added to that position in the track list.
                otherwise song will added at the end of the list.
            :return: None
        """

        if position is None:
            self.track.append(song)
        else:
            self.track.insert(position, song)


class Artist:
    """Basic class to store artist details.
    Attributes:
        name (str): The name of the artist.
        albums (List(Album)): A list of album by the artist.
            The list includes those albums in this collection,
            it is not an exhaustive list of the artist's published albums.
    Methods:
        add_album: Use to add a new album to the artist's albums List.
    """

    def __init__(self, name):
        self.name = name
        self.albums = list()

    def add_album(self, album):
        """ Add a new album to the list.
        Args:
            :param album: An album object to add to the list. If album is present we don't add again
            :return:None
        """
        if album not in self.albums:
            self.albums.append(album)


def find_object(field, object_list):
    """Check 'object_list' to see if the 'name' attribute is equal to 'field' exists. That means the object already exists.
        We will retrieve the object and return on function call.
    """
    for item in object_list:
        if item.name == field:
            return item
    return None  # if nothing matches return 'None' after all loop execution.

#
# def load_data():
#     """It loads artists from the albums.txt"""
#     new_artist = None
#     new_album = None
#     artist_list = list()
#     with open('albums.txt', 'r') as albums:
#         for line in albums:
#             # Data row consists of (artists, album, year, song)
#             artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
#             year_field = int(year_field)
#             if new_artist is None:
#                 new_artist = Artist(artist_field)
#             elif new_artist.name != artist_field:
#                 # We have just read details of a new artist.
#                 # Store current album in artist collections and create a new artist object
#                 new_artist.add_album(new_album)
#                 artist_list.append(new_artist)
#                 new_artist = Artist(artist_field)
#                 new_album = None
#
#             if new_album is None:
#                 new_album = Album(album_field, year_field, new_artist)
#             elif new_album.name != album_field:
#                 # We just read new album of the current artist
#                 # Store current album in artist collections and create a new artist object
#                 new_artist.add_album(new_album)
#                 new_album = Album(album_field,year_field, new_artist)
#
#             # Now creating new Song object and adding in current album collection
#             new_song = Song(song_field, artist_field)
#             new_album.add_song(new_song)
#
#     # After reading the last line of the file we will have artist and album that haven't been stored
#         if new_artist is not None:
#             if new_album is not None:
#                 new_artist.add_album(new_album)
#             artist_list.append(new_artist)
#
#     return artist_list


def load_data():
    """We are using new approach to load data using find_object method. First we will insert the object inside the
     list and hen retrieve it.
     This load method is capable to store even unordered data
     file into ordered file having all the albums of one artist together"""
    new_artist = None
    new_album = None
    artist_list = list()

    with open("albums.txt", 'r') as album_file:
        for line in album_file:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist != artist_field:
                # We have just read details of a new artist.
                # retrieve artist object if there is one or else make a new object and append in list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    # Make a new one
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, artist_field)
                new_artist.albums.append(new_album)
            elif new_album != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, artist_field)
                    new_artist.albums.append(new_album)
            new_song = Song(song_field, artist_field)
            new_album.add_song(new_song)
    return artist_list


def create_check_file(artists):
    with open("check_file.txt", 'w') as check_file:
        for new_artist in artists:
            for new_album in new_artist.albums:
                for new_song in new_album.track:
                    print("{0.name}\t{1.name}\t{2.year}\t{3.title}".
                          format(new_artist, new_album, new_album, new_song), file=check_file)


if __name__ == '__main__':
    artist_list = load_data()
    for artist in artist_list:
        print(artist.name)
        for album in artist.albums:
            print("\t"+album.name)
            for song in album.track:
                print("\t\t", song.title)
    create_check_file(artist_list)

    """ This program is not fully Object oriented we will make it in Song_version2.py
    """
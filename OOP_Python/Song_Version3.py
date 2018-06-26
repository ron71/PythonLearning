"""
To remove the circular reference we must remove the Artist reference from the album class and Song Class.
We will change the artist reference to artist name in Song and Album Class.
"""


class Song:
    """ Class to represent the song
        Attributes:
        title (str)-  The title of the song
        artist (str)- The artist of the song
        duration (int) - Duration of the song

    """

    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title) # This allows the program to access getter method for title using name keyword
    # we are doing so because our find_object method is a generic method which deal with name of the instances.


class Album:
    """ Class to represent album using it's track lists.

    Attributes:
        name (str) : The name of the album
        year (int): the year of the album released.
        artist (str): The artist responsible for the album.
            if not specified, the artist will default to an artist wit name "Various Artists"
        track (List[Song]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
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
        song_found = find_object(song, self.track)
        # we are searching the song in the album to avoid duplication.
        # Due to presence of the song more then once in the file.
        if song_found is None:
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

    def add_song(self, album, year, song, position=None):
        # for temp_album in self.albums:
        #     if temp_album.name == album:
        #         temp_song = Song(song, self)
        #         temp_album.add_song(temp_song)
        #         return
        # # if album is not present
        # temp_album = Album(album, year, self)
        # temp_song = Song(song, self)
        # temp_album.add_song(temp_song)
        # self.add_album(temp_album)    # These commented part are my version of code

        album_found = find_object(album, self.albums)
        if album_found is None:
            album_found = Album(album, year, self.name)
            temp_song = Song(song, self.name)
            album_found.add_song(temp_song)
            self.add_album(album_found)
        else:
            temp_song = Song(song, self.name)
            album_found.add_song(temp_song)

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
    # print(len(object_list))
    for item in object_list:
        if item.name == field:
            return item
    return None  # if nothing matches return 'None' after all loop execution.


def load_data():
    """We are using new approach to load data using find_object method. First we will insert the object inside the
     list and hen retrieve it.
     This load method is capable to store even unordered data
     file into ordered file having all the albums of one artist together"""
    artist_list = list()

    with open("albums.txt", 'r') as album_file:
        for line in album_file:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            new_artist = find_object(artist_field, artist_list)
            if new_artist is not None:
                # print(new_artist.name)
                new_artist.add_song(album_field, year_field, song_field)
            else:
                new_artist = Artist(artist_field)
                new_artist.add_song(album_field, year_field, song_field)
                artist_list.append(new_artist)

    return artist_list


def create_check_file(artists):

    with open("check_file_for_version3.txt", 'w') as check_file:
        for new_artist in artists:
            for new_album in new_artist.albums:
                # print(len(new_artist.albums))
                for new_song in new_album.track:
                    print("{0.name}\t{1.name}\t{2.year}\t{3.title}".
                          format(new_artist, new_album, new_album, new_song), file=check_file)


if __name__ == '__main__':
    artist_list = load_data()
    for artist in artist_list:
        print(artist.name + "\n***************************************")
        for album in artist.albums:
            print("\t"+album.name + "\n***************************************")
            for song in album.track:
                print("\t\t", song.title)

    create_check_file(artist_list)


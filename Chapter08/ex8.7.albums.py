# Python Crash Course, 2Ed, writtern by Eric Matthes

albums = []

def make_album (album_name, artist):
    album = {}
    album['album_name'] = album_name
    album['artist'] = artist
    album['no_of_songs'] = None
    return album

def print_album(albums):
    for album in albums:
        if album['no_of_songs'] != None:
            print(f"{album['album_name']} of {album['artist']} has number of songs: {album['no_of_songs']}")
        else:
            print(f"{album['album_name']} of {album['artist']} has no songs.") 

albums.append(make_album('Beam of Prism', 'VIVIZ'))
albums.append(make_album('Summer Vibe', 'VIVIZ'))
albums.append(make_album('VarioUS', 'VVIZ'))

albums[0]['no_of_songs'] = 7

print_album(albums)

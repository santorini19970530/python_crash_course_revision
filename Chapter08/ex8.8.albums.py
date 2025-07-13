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
            print(f"\"{album['album_name']}\" of {album['artist']} has number of songs: {album['no_of_songs']}")
        else:
            print(f"\"{album['album_name']}\" of {album['artist']} has no songs.") 

albums.append(make_album('Beam of Prism', 'VIVIZ'))
albums.append(make_album('Summer Vibe', 'VIVIZ'))
albums.append(make_album('VarioUS', 'VVIZ'))
albums[0]['no_of_songs'] = 7

while True:
    print("Enter detail of an album.")
    print("(enter \'q\' at any time to quit)")

    album_name = input("Album Name: ")
    if album_name == 'q':
        break

    artist = input("Artist Name: ")
    if artist == 'q':
        break

    no_of_songs = input("No. of Albums: ")
    if no_of_songs == 'q':
        break
    elif no_of_songs == '0':
        no_of_songs = None
    
    albums.append(make_album(album_name, artist))
    if no_of_songs != None:
        albums[-1]['no_of_songs'] = int(no_of_songs)

print("\n")
print_album(albums)

# Hive Radio
import MusicHandler
import PlaylistHandler

with open("constants.txt","r") as file:
    API_KEY = file.read().split("\n")
    print(API_KEY)
DESTINATION_PATH = "./Songs/SongList"

"""
IMPORTANT: Use the link: https://www.spotlistr.com/export/spotify-playlist
copy the name of the song and the artist into the SongList.txt file in Songs directory
and add an API key to the program
"""


def main():
    """
    Downloads all the songs in the SongList.txt inside the Songs directory
    :return: None
    """
    print("Use the following link to format your songs: https://www.spotlistr.com/export/spotify-playlist")

    print("***************************Hive*Radio***************************")
    try:
        with open("./Songs/SongList.txt", 'r') as file:
            for song in file.read().split("\n"):
                video_name = PlaylistHandler.get_first_youtube_link_api(song, API_KEY)
                MusicHandler.download_video(video_name, DESTINATION_PATH)
    except Exception as e:
        print(f"error - {e}")
    print("****************************************************************")


if __name__ == "__main__":
    main()

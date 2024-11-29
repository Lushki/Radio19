# Hive Radio
import MusicHandler
import PlaylistHandler

API_KEY = "AIzaSyAoUtUawnPL0U2_b2XqHGpfsefkMjn7EDE"
DESTINATION_PATH = "./Songs/SongList"

"""
IMPORTANT: Use the link: https://www.spotlistr.com/export/spotify-playlist
copy the name of the song and the artist into the SongList.txt file in Songs directory
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

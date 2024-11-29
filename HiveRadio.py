# Hive Radio
import MusicHandler
import PlaylistHandler

API_KEY = "AIzaSyAoUtUawnPL0U2_b2XqHGpfsefkMjn7EDE"
# https://www.spotlistr.com/export/spotify-playlist

def main():
    print("***************************Hive*Radio***************************")
    try:
        with open("./SongList.txt", 'r') as file:
            for song in file.read().split("\n"):
                video_name = PlaylistHandler.get_first_youtube_link_api(song, API_KEY)
                MusicHandler.download_video(video_name)
    except Exception as e:
        print(f"error - {e}")
    print("****************************************************************")


if __name__ == "__main__":
    main()

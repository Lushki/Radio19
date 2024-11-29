# Hive Radio
import MusicHandler
import PlaylistHandler

API_KEY = "AIzaSyAoUtUawnPL0U2_b2XqHGpfsefkMjn7EDE"


def main():
    print("***************************Hive*Radio***************************")
    try:
        video_name = input("Enter Video Name: \n>> ")
        video_name = PlaylistHandler.get_first_youtube_link_api(video_name, API_KEY)
        MusicHandler.download_video(video_name)
    except Exception as e:
        print(f"error - {e}")
    print("****************************************************************")


if __name__ == "__main__":
    main()

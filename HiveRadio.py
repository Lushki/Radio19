# Hive Radio
import MusicHandler
import PlaylistHandler


def main():
    print("***************************Hive*Radio***************************")
    try:
        video_link = input("Enter the URL of the video you want to download: \n>> ")
        MusicHandler.download_video(video_link)
    except Exception as e:
        print(f"error - {e}")
    print("****************************************************************")


if __name__ == "__main__":
    main()

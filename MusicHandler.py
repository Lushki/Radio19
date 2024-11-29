# importing packages
from pytubefix import YouTube
import os


def download_video(video_link: str, dest_path):
        """
        Downloads YouTube videos from link to the given location.
        :param video_link:
        :param dest_path:
        :return:
        """
        yt = YouTube(str(video_link))

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # check for destination to save file
        destination = dest_path

        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.wav'
        os.rename(out_file, new_file)

        # result of success
        print("[" + yt.title + " has been successfully downloaded.]")





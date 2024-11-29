from googleapiclient.discovery import build


def get_first_youtube_link_api(query, api_key):
    """
    fetches the link to the title given on YouTube
    :param query:
    :param api_key:
    :return: a YouTube link
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    # Correct method to call search().list
    request = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=1,
        type='video'  # Ensures we get video results only
    )
    response = request.execute()
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return "No video found"

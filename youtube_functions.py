from googleapiclient.discovery import build
from Api_key import YOUTUBE_API_KEY

def search_youtube_video(query):
    """
    Search for a YouTube video using the YouTube Data API.
    :param query: The search query (e.g., workout title or keyword).
    :return: The title and URL of the first video found.
    """
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    # Search for the video
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=1
    )
    response = request.execute()
    
    # Extract video information
    if response['items']:
        video = response['items'][0]
        title = video['snippet']['title']
        video_id = video['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return title, video_url
    else:
        return None, None


import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi


def get_subtitles(link):
    unique_id = link.split("=")[-1]
    sub = YouTubeTranscriptApi.get_transcript(unique_id)  
    subtitle = " ".join([x['text'] for x in sub])
    return subtitle
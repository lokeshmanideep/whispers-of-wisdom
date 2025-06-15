import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os
from constants import FILE_PATH, TITLE, DESCRIPTION, THUMBNAIL_PATH
from dotenv import load_dotenv
load_dotenv()
def get_authenticated_service():
    scopes = ["https://www.googleapis.com/auth/youtube.upload","https://www.googleapis.com/auth/youtube"]
    SECRET_PATH = os.getenv("SECRET_PATH")
    flow = InstalledAppFlow.from_client_secrets_file(
        SECRET_PATH, scopes)
    credentials = flow.run_local_server(port=8080)
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
def upload_video(youtube,file_path, title, description, tags, category_id="22", privacy_status="private"):
    # Get credentials and create API client

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }

    media_file = MediaFileUpload(file_path, resumable=True, chunksize=-1)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploading... {int(status.progress() * 100)}%")

    video_id = response.get("id")
    print("✅ Upload complete, video ID:", video_id)
    return video_id

def set_thumbnail(youtube, video_id, thumbnail_path):
    request = youtube.thumbnails().set(
        videoId=video_id,
        media_body=MediaFileUpload(thumbnail_path)
    )
    response = request.execute()
    print("📸 Thumbnail set.")
def add_to_playlist(youtube, video_id, playlist_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    request.execute()
    print("📺 Added to playlist.")


# Usage

if __name__ == "__main__":
    youtube = get_authenticated_service()

    video_id = upload_video(
        youtube,
        file_path=FILE_PATH,
        title=TITLE,
        description=DESCRIPTION,
        tags=["Justice", "Revenge", "Anger", "Compassion", "Dharma", "Emotional Intelligence"]
    )
    # Set thumbnail
    set_thumbnail(youtube, video_id, thumbnail_path=THUMBNAIL_PATH)

    # Add to playlist
    add_to_playlist(youtube, video_id, playlist_id="PLPgC7mD72GJ_rUG0khmdx-7CNDjRmxu-X")
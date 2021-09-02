import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_api_call(keywords):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = 'YOUR_APIKEY')

    first_values = list(keywords.keys())
    print(first_values)
    query = ",".join(first_values)
    youtuberequest = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=query
    )
    response = youtuberequest.execute()
    return response

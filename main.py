import requests

def print_if_question(text):
    keywords = ['how', 'what', 'when', 'why']
    lower_text = text.lower()
    if any(word in lower_text for word in keywords) or '?' in text:
        return text
    return None

API_KEY = 'AIzaSyApkT34sHrCVEskQUxnM-_nhMqJnJ3cmG4'
VIDEO_ID = '0A_GCXBCNUQ'
BASE_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

params = {
    'part': 'snippet',
    'videoId': VIDEO_ID,
    'maxResults': 100,
    'key': API_KEY
}

while True:
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    for item in data.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        result = print_if_question(comment)
        if result:
            print(result)
            print("=============================")

    if 'nextPageToken' in data:
        params['pageToken'] = data['nextPageToken']
    else:
        break

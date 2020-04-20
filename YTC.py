import urllib3
import json
from bs4 import BeautifulSoup

YOUTUBE_URL = 'https://www.youtube.com'

def get_track_description(track_url):
  url = YOUTUBE_URL + track_url
  req = urllib3.PoolManager()
  res = req.request('GET', url)
  soup = BeautifulSoup(res.data.decode('utf-8'),'html.parser')
  description = soup.find(id='eow-description')
  if not description:
    return 'No description'
  return description.text.strip()

def get_playlist_data(playlist_url,description=True):
  response = []
  url = YOUTUBE_URL + playlist_url
  req = urllib3.PoolManager()
  res = req.request('GET', url)
  soup = BeautifulSoup(res.data.decode('utf-8'),'html.parser')
  list = soup.find_all("tr",class_="pl-video yt-uix-tile")
  for item in list:
    track_info = item.find('td',class_='pl-video-title')
    track_length = item.find('td',class_='pl-video-time')
    track_length = track_length.find('span').text
    track_link = track_info.find('a')
    track_url = track_link['href']
    track_name = track_link.text.strip()
    if description:
      response.append({
        'track_name':track_name,
        'track_url':YOUTUBE_URL + track_url,
        'track_length':track_length,
        'track_description':get_track_description(track_url)
      })
    else:
      response.append({
        'track_name':track_name,
        'track_url':YOUTUBE_URL + track_url,
        'track_length':track_length,
      })
    json.dumps(response)
  return response

def get_channel_playlists(channel_url,tracks=True,description=True):
  response = {
    'channel_name':'',
    'playlists':[]
  }
  req = urllib3.PoolManager()
  res = req.request('GET', channel_url)
  soup = BeautifulSoup(res.data.decode('utf-8'),'html.parser')
  channel_name = soup.find('a',class_='spf-link branded-page-header-title-link yt-uix-sessionlink')
  response['channel_name'] = channel_name
  list = soup.find('ul',class_='channels-browse-content-grid branded-page-gutter-padding grid-lockups-container')
  list_items = list.find_all('li',class_='channels-content-item yt-shelf-grid-item')
  for item in list_items:
    playlist_info = item.find('h3',class_='yt-lockup-title')
    palylist_link = playlist_info.find('a')
    palylist_url = palylist_link['href']
    playlist_name = palylist_link['title'].strip()
    if tracks:
      response['playlists'].append({
        'playlist_name':playlist_name,
        'playlist_url':YOUTUBE_URL + palylist_url,
        'playlist_tracks':get_playlist_data(palylist_url,description)
      })
    else:
      response['playlists'].append({
        'playlist_name':playlist_name,
        'playlist_url':YOUTUBE_URL + palylist_url,
      })
  return response

json_object = json.dumps(get_channel_playlists('https://www.youtube.com/user/amrkomar/playlists'))
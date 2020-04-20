import ytc

# Get track description box by passing track url excluding (www.youtube.com) part 
track_description = ytc.get_track_description('/watch?v=7d16CpWp-ok')


# Get playlist tracks, duration and description as python dict by passing playlist url excluding (www.youtube.com) part 
playlist_tracks_default = ytc.get_playlist_tracks('/playlist?list=FLxBR44IXdJY0gsfHcIDMQuQ')


# response could be also represented as json
# gettting tracks description could be neglicted which saves a lot of crawling time
playlist_tracks_options = ytc.get_playlist_tracks('/playlist?list=FLxBR44IXdJY0gsfHcIDMQuQ', json_response=True, description=False)


# uncomment next lines to save playlist_tracks_options json result to json file
# with open('example-playlist_tracks_options.json','w',encoding='utf-8') as f:
#     f.write(playlist_tracks_options)
#     f.close()

# Get channel playlists, tracks, duration and description as python dictby passing channel playlits url excluding (www.youtube.com) part 
channel_playlists_default = ytc.get_channel_playlists('/user/lebo2196/playlists')

# response could be also represented as json
# getting tracks is optional
# gettting tracks description could be neglicted which saves a lot of crawling time
# NOTE : description will not be effective unless tracks flag is True
channel_playlists_options = ytc.get_channel_playlists('/user/lebo2196/playlists',json_response=True, tracks=False, description=False)

# uncomment next lines to save channel_playlists_options json result to json file
# with open('example-channel_playlists_options.json','w',encoding='utf-8') as f:
#     f.write(channel_playlists_options)
#     f.close()
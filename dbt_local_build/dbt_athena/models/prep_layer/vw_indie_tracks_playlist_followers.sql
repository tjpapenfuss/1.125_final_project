SELECT 
t1.track_id As TrackId, t1.track_name, t1.popularity,
t2.playlist_id, t2.playlist_name, t2.total_followers
FROM "raw_data_spotify_dataset"."spotify_indie_playlist_tracks_data_csv_bucket" t1  
LEFT JOIN "raw_data_spotify_dataset"."spotify_indie_playlist_data_csv_bucket" t2
ON t1.playlist_id = t2.playlist_id
group by t1.track_id, t2.playlist_id, t1.track_name, t2.total_followers, t1.popularity, t2.playlist_name

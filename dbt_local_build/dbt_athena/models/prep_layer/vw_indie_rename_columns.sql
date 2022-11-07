-- Drop some columns and renaming the rest

SELECT "playlist_name" AS Playlist,
       "playlist_id",
       "total_followers"  AS Followers
FROM "raw_data_spotify_dataset"."spotify_indie_playlist_data_csv_bucket"

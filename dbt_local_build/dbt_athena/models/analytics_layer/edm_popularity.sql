
SELECT playlist_id, playlist_name, AVG(popularity) as AvgPop
FROM {{ ref('vw_edm_tracks_playlist_followers') }}
GROUP BY playlist_id, playlist_name
limit 10;


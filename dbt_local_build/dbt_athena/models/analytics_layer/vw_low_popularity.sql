SELECT  playlist_id, playlist_name, AvgPop, Genre
FROM
        (
            SELECT  playlist_id, playlist_name, AvgPop, 'EDM' as Genre FROM {{ ref('edm_popularity') }}
            UNION ALL
            SELECT  playlist_id, playlist_name, AvgPop, 'INDIE' as Genre FROM {{ ref('indie_view_popularity') }}
            UNION ALL
            SELECT  playlist_id, playlist_name, AvgPop, 'Jazz' as Genre FROM {{ ref('jazz_view_popularity') }}
        ) s
WHERE AvgPop < 40
GROUP BY AvgPop, playlist_id, playlist_name, Genre
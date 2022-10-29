-- Create sentiment score

SELECT Playlist_id,
       Playlist,
       CASE WHEN Followers    BETWEEN 0 AND 1000        THEN -1
            WHEN Followers  BETWEEN 1000 AND 5000       THEN 0
            WHEN Followers  > 5000                      THEN 1
            ELSE NULL
       END                                  AS Popularity
FROM {{ ref('vw_edm_rename_columns') }}












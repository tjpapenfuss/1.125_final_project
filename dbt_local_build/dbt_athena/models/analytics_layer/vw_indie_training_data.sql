-- Remove records with sentiment score in NULL
SELECT *
FROM {{ ref('vw_indie_popularity') }}
WHERE Popularity             IS NOT NULL
AND Playlist_id        IS NOT NULL
-- AND PRODUCT_CATEGORY IN (
--     SELECT PRODUCT_CATEGORY
--     FROM {{ ref('vw_indie_popularity') }}
--     GROUP BY PRODUCT_CATEGORY
--     HAVING COUNT(*) >20
--     )




-- Lists all genres and displays number of shows linked
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;

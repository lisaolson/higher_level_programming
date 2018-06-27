-- List all shows and all genres linked to that show from hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name ASC;

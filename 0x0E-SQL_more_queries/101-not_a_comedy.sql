-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT tv_shows.title
FROM tv_shows INNER JOIN (SELECT tv_show_genres.show_id FROM tv_show _genres OUTER JOIN
	(SELECT tv_show_genres.show_id FROM tv_show_genres INNER JOIN tv_genres 
	on tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy") ON tv_show_genres.genre_id = tv_show_genres.genre_id WHERE tv_show_genres.genre_id IS NULL)
on tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title;

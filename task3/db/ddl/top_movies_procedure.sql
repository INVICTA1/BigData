USE `movies`;

DROP PROCEDURE if exists usp_find_top_rated_movies;
DELIMITER \\
CREATE PROCEDURE usp_find_top_rated_movies(n INT, regex VARCHAR(50), year_from INT, year_to INT, genres VARCHAR(100))
BEGIN
	drop temporary table if exists temp_movies;
	create temporary table temp_movies(	`id` 		INT UNIQUE NOT NULL,
										`name` 		VARCHAR(200) NOT NULL,
										`year` 		INT,
										`genres`	VARCHAR(100),
										`rating` 	FLOAT );
	INSERT into temp_movies SELECT * from `movies`.`movies`;
	IF regex IS NOT NULL THEN
			with regex_movies as (select * from `movies`.`movies` where REGEXP_INSTR(name,regex,1,1,0,'i') = 0)
            DELETE temp_movies from  temp_movies  JOIN regex_movies on   temp_movies.id = regex_movies.id;
	END IF;
	IF genres IS NOT NULL THEN
			call `movies`.filter_by_genres(genres);
			DELETE temp_movies from  temp_movies  JOIN temp_table on   temp_movies.id = temp_table.id;
	END IF;
	IF year_from IS NOT NULL THEN
			DELETE from temp_movies where `year` < year_from;
	END IF;
	IF year_to IS NOT NULL THEN
			DELETE from temp_movies where `year` > year_to;
	END IF;
	IF n IS NOT NULL and genres IS NOT NULL  THEN
			call `movies`.sort_by_number_genres(n, genres);
            select * from temp_table;
	ELSEIF n IS NOT NULL THEN
			select * from temp_movies order by rating DESC limit n;
	ELSEIF n IS NULL THEN
			select * from temp_movies order by rating DESC ;
	END IF;
	drop temporary table if exists temp_table;
    drop temporary table if exists temp_movies;
END
\\
DELIMITER ;

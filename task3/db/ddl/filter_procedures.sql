USE `movies`;
DROP PROCEDURE if exists filter_by_genres;
DROP PROCEDURE if exists sort_by_number_genres;


DELIMITER \\

create procedure filter_by_genres(genres varchar(200))
begin
	DECLARE num INT DEFAULT 0;
	DECLARE num_genres INT;
    DECLARE genre VARCHAR(50);
    DROP temporary table if  exists temp_table;
    create temporary table temp_table(`id` 		INT UNIQUE NOT NULL,
									  `name` 	VARCHAR(200) NOT NULL,
									  `year` 	INT,
									  `genres`	VARCHAR(100),
									  `rating` 	FLOAT );
	set num_genres := (CHAR_LENGTH(genres) - CHAR_LENGTH(REPLACE(genres,'|',''))) div CHAR_LENGTH('|');
    WHILE  num <= num_genres DO
    set num = num + 1;
    set  genre := SUBSTRING_INDEX(genres,'|',1);
    INSERT IGNORE INTO temp_table select * from temp_movies where  REGEXP_INSTR(temp_movies.genres,genre,1,1,0,'i') = 0;
    set genres :=  SUBSTRING(genres, - (LENGTH(genres) - LENGTH(genre) - 1));
    END WHILE;
end;
\\

create procedure sort_by_number_genres(n int, genres varchar(200))
begin
	DECLARE num INT DEFAULT 0;
	DECLARE num_genres INT;
    DECLARE genre VARCHAR(50);
    DROP temporary table if  exists temp_table;
    create temporary table temp_table(`id` 		INT  NOT NULL,
									  `name` 	VARCHAR(200) NOT NULL,
									  `year` 	INT,
									  `genres`	VARCHAR(100),
									  `rating` 	FLOAT );
	set num_genres :=  (CHAR_LENGTH(genres) - CHAR_LENGTH(REPLACE(genres,'|',''))) div CHAR_LENGTH('|');

    WHILE  num <= num_genres DO
    set num = num + 1;
    set  genre := SUBSTRING_INDEX(genres,'|',1);
    INSERT INTO temp_table select * from temp_movies where  REGEXP_INSTR(temp_movies.genres,genre,1,1,0,'i') order by rating DESC limit n;
    set genres :=  SUBSTRING(genres, - (LENGTH(genres) - LENGTH(genre) - 1));
    END WHILE;
end;
\\
DELIMITER ;

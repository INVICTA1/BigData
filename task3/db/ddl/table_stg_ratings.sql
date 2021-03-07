USE `stg_movies`;

CREATE TABLE `stg_ratings`(`user_id` 	INT NOT NULL,
						   `movie_id` 	INT NOT NULL,
						   `rating` 	FLOAT NOT NULL,
						   `timestamp`  int NOT NULL,
						   index `movie_id_index` (`movie_id`));
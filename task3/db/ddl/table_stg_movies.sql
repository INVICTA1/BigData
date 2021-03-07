USE `stg_movies`;

CREATE TABLE `stg_movies`(`id` 		INT UNIQUE NOT NULL ,
						  `title` 	VARCHAR(200) not null,
						  `genres` 	VARCHAR(100));
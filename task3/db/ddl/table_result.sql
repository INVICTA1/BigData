USE `movies`;

CREATE TABLE `result`(	`id` 		INT UNIQUE NOT NULL,
						`name` 		VARCHAR(200) NOT NULL,
						`year` 		INT,
                        `genres`	VARCHAR(100),
						`rating` 	FLOAT );
USE `stg_movies`;

WITH  average_rating as (select `movie_id`,round(avg(`rating`),2) as avg_rating  from stg_ratings group by `movie_id` )
UPDATE  `movies`.`movies`, average_rating
SET `movies`.`rating` = average_rating.avg_rating
WHERE `movies`.`id`=average_rating.movie_id;
USE `stg_movies`;

DELIMITER //

CREATE TRIGGER split_title
AFTER INSERT ON `stg_movies`
FOR EACH ROW
	BEGIN
    set @`regex` := '\\(\\d{4}\\)|\\(\\d{4}-\\d{4}\\)';
	SET @`id` := NEW.`id`;
	SET @`year` := REGEXP_SUBSTR (NEW.`title`,@`regex` );
	IF  LENGTH(@`year`) = 6   THEN
		SET @`year` := SUBSTRING(@`year`,2,4);
		SET @`name` := REGEXP_REPLACE(NEW.`title`,@`regex`,'');
	ELSEIF  LENGTH(@`year`) = 11 THEN
		SET @`year` := SUBSTRING(@`year`,7,4);
        SET @`name` := REGEXP_REPLACE(NEW.`title`,@`regex`,'');
	END IF ;
    INSERT INTO `movies`.`movies`(`id`,`name`,`year`,`genres`) VALUES(NEW.id,@`name`,@`year`,NEW.`genres`);
	END
  //
DELIMITER ;

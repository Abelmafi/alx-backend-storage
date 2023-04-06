-- The CREATE FUNCTION statement creates a function named SafeDiv that takes two arguments a and b of data type INT.
-- The RETURNS INT clause specifies that the function returns an integer value.
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF b != 0 THEN
        SET result = a / b;
    END IF;
    RETURN result;
END $$
DELIMITER ;

-- The CREATE FUNCTION statement creates a function named SafeDiv that takes two arguments a and b of data type INT.
-- The RETURNS INT clause specifies that the function returns an integer value.
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;

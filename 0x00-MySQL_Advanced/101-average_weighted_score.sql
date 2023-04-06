-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- 
-- Requirements:
-- 
--     Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE sum_weighted_score FLOAT DEFAULT 0;
    DECLARE sum_weights FLOAT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
    INTO sum_weighted_score, sum_weights
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id;

    UPDATE users
    SET average_score = IF(sum_weights = 0, 0, sum_weighted_score / sum_weights);

END $$
DELIMITER ;

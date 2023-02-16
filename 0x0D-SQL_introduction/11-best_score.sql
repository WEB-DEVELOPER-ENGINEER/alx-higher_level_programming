-- List all records with score >= 10 in 'second_table' of db 'hbtn_0c_0'
-- Results should display both score and name
-- Records should be ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

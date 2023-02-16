-- List number of records with same score in 'second_table'
SELECT DISTINCT score, COUNT(*) WHERE score = score as number FROM second_table ORDER BY number DESC;

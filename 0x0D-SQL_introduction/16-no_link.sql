-- List all records of the table without a name value
SELECT score, name
FROM second_table
WHERE EXISTS (SELECT name FROM second_table WHERE name = second_table.name)
ORDER BY score DESC;

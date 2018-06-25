-- Display the number of records with id=89 in the table
SELECT id AS "id",
	COUNT(id) AS "num ids"
FROM first_table
WHERE id=89

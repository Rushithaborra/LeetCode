SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        ROW_NUMBER() OVER (ORDER BY id) -
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS Grp
    FROM Logs
) t
GROUP BY num, Grp
HAVING COUNT(*) >= 3;
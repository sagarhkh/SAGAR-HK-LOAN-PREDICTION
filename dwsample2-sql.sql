
 
---------
 

——————

SELECT
    CASE
        WHEN narrative LIKE '%hospital%' OR narrative LIKE '%medical expenses%' THEN
            CASE
                WHEN strftime('%H:%M:%S', time) >= '00:00:00' AND strftime('%H:%M:%S', time) < '03:00:00' THEN 'midnight hour'
                ELSE 'daytime'
            END
        ELSE 'daytime'
    END AS time_category
FROM [data sb$];

————-
-- Assuming your Excel file is connected to SQLite
-- If you're using a different database, syntax may vary

-- Compare the time column for "hospital" and "medical expenses" and retu
SELECT
    CASE
        WHEN narrative LIKE '%hospital%' AND strftime('%H:%M:%S', time) >= '00:00:00' AND strftime('%H:%M:%S', time) < '03:00:00' THEN 'midnight hour'
        WHEN narrative LIKE '%medical expenses%' AND strftime('%H:%M:%S', time) >= '00:00:00' AND strftime('%H:%M:%S', time) < '03:00:00' THEN 'midnight hour'
        ELSE NULL -- or provide another default value
    END AS midnight_hour
FROM [data sb$];
———-
-- Assuming your Excel file is connected to SQLite
-- If you're using a different database, syntax may vary

-- Calculate the count for each keyword and sum them up
SELECT
    SUM(
        CASE
            WHEN narrative LIKE '%hospital%' THEN 1
            WHEN narrative LIKE '%Zomato%' THEN 1
            WHEN narrative LIKE '%Swiggy%' THEN 1
            WHEN narrative LIKE '%medical expenses%' THEN 1
            WHEN narrative LIKE '%hotel%' THEN 1
            ELSE 0
        END
    ) AS red_flags
FROM [data sb$];

——-

 
-- Calculate the count for each keyword and sum them up
SELECT
    (SELECT COUNT(*) FROM [data sb$] WHERE narrative LIKE '%hospital%') +
    (SELECT COUNT(*) FROM [data sb$] WHERE narrative LIKE '%Zomato%') +
    (SELECT COUNT(*) FROM [data sb$] WHERE narrative LIKE '%Swiggy%') +
    (SELECT COUNT(*) FROM [data sb$] WHERE narrative LIKE '%medical expenses%') +
    (SELECT COUNT(*) FROM [data sb$] WHERE narrative LIKE '%hotel%') AS red_flags;


——


 
-- Checking transaction activities in Daytime hours
SELECT
    CASE
        WHEN Narration LIKE '%hospital%' OR Narration LIKE '%medical expenses%' THEN
            CASE
                WHEN strftime('%H:%M:%S', time) >= '00:00:00' AND strftime('%H:%M:%S', time) < '03:00:00' THEN 'midnight hour'
                ELSE 'daytime'
            END
        ELSE 'daytime'
    END AS time_category
FROM [GITHUB EXCEL CSV$];


-- Checking transaction activities in midnight hours
SELECT
    CASE
        WHEN Narration LIKE '%zomato%' AND strftime('%H:%M:%S', time) >= '00:00:00' AND strftime('%H:%M:%S', time) < '03:00:00' THEN 'midnight hour'
        WHEN Narration LIKE '%ola/uber%' AND strftime('%H:%M:%S', time) >= '00:00:00' AND strftime('%H:%M:%S', time) < '03:00:00' THEN 'midnight hour'
        ELSE NULL -- or provide another default value
    END AS midnight_hour
FROM [GITHUB EXCEL CSV$];
———-
 
 
-- Calculate the count for each keyword and sum them up
SELECT
    (SELECT COUNT(*) FROM [GITHUB EXCEL CSV$] WHERE Narration LIKE '%hospital%') +
    (SELECT COUNT(*) FROM [GITHUB EXCEL CSV$] WHERE Narration LIKE '%Zomato%') +
    (SELECT COUNT(*) FROM [GITHUB EXCEL CSV$] WHERE Narration LIKE '%Swiggy%') +
    (SELECT COUNT(*) FROM [GITHUB EXCEL CSV$] WHERE Narration LIKE '%medical expenses%') +
    (SELECT COUNT(*) FROM [GITHUB EXCEL CSV$] WHERE Narration LIKE '%hotel%') AS red_flags;

 -- Count occurrences and calculate sum of all red flag expenses to variable-"red_flag_expense"
SELECT
    COUNT(CASE WHEN Narration LIKE '%hospital%' OR Narration LIKE '%Zomato%' OR Narration LIKE '%Swiggy%' OR Narration LIKE '%medical expenses%' OR Narration LIKE '%hotel%' THEN 1 END) AS red_flags,
    SUM(amount) AS red_flag_expense
FROM [GITHUB EXCEL CSV$];

SELECT COUNT(*) AS "Number Of Listings", n.name as "Neighborhood"
FROM Listings l
JOIN Neighborhoods n ON l.neighborhood_id = n.id
GROUP BY n.id;
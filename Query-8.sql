SELECT AVG(l.price) AS "Average Price", n.name as "Neighborhood Name"
FROM Listings l
JOIN Neighborhoods n ON l.neighborhood_id = n.id
GROUP BY n.id
ORDER BY "Average Price" DESC
LIMIT 5;
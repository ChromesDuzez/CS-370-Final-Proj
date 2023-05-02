SELECT h.name as "Host Name", COUNT(*) as "Total Reviews"
FROM Reviews r
INNER JOIN Listings l ON r.listing_id = l.id
INNER JOIN Hosts h ON l.host_id = h.id
GROUP BY l.host_id
ORDER BY COUNT(*) DESC
LIMIT 10;
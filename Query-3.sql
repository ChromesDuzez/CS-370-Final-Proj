SELECT COUNT(*) AS "Number Of Reviews", l.id as "Listing ID", l.name as "Listing"
FROM Reviews r
JOIN Listings l ON r.listing_id = l.id
GROUP BY r.listing_id
ORDER BY "Number Of Reviews" DESC
LIMIT 5;
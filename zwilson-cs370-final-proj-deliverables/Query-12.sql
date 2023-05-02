SELECT l.name, CAST(COUNT(*) AS DECIMAL(7,2))/l.minNights * 1.0 AS "Number of Reviews, Minimum Nights Correl", l.minNights, COUNT(*) AS "Total Reviews"
FROM listings l
JOIN reviews r ON l.id = r.listing_id
GROUP BY r.listing_id
ORDER BY "Number of Reviews, Minimum Nights Correl" DESC
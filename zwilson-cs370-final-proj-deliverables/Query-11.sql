SELECT l.name as "Listing", strftime('%m', date(r.datePosted)) AS month, COUNT(*) AS num_reviews, l.availability 
FROM Listings l INNER JOIN Reviews r on l.id = r.listing_id 
GROUP BY l.id, month 
ORDER BY l.name, num_reviews DESC;
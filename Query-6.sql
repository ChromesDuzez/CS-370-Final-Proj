SELECT "Neighborhood Name", "Listing ID", "Listing", "Average Score"
FROM (
  SELECT n.name as "Neighborhood Name", l.id as "Listing ID", l.name as "Listing", count(r.id) AS "Average Score", ROW_NUMBER() OVER (PARTITION BY n.id ORDER BY "Average Score" DESC) AS rank
  FROM Reviews r
  INNER JOIN Listings l on r.listing_id = l.id
  INNER JOIN Neighborhoods n on l.neighborhood_id = n.id
  GROUP BY l.neighborhood_id, l.id
) subquery
WHERE rank = 1;
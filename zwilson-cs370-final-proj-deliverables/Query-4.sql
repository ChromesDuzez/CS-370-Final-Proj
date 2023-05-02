SELECT * 
FROM (
	SELECT COUNT(*) AS "NumberOfListings", h.name as "Host"
	FROM Listings l
	INNER JOIN Hosts h on l.host_id = h.id
	GROUP BY l.host_id
	ORDER BY "NumberOfListings" DESC
) subsel
WHERE subsel.NumberOfListings > 1;
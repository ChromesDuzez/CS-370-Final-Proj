SELECT n.name as "Neighborhood Name",
    AVG(CASE WHEN r.roomType = "Private room" THEN l.price ELSE NULL END) as "Private Room Price",
    AVG(CASE WHEN r.roomType = "Entire home/apt" THEN l.price ELSE NULL END) as "Entire home/apt Price",
    AVG(CASE WHEN r.roomType = "Entire home/apt" THEN l.price ELSE NULL END) - AVG(CASE WHEN r.roomType = "Private room" THEN l.price ELSE NULL END) as "Price Difference"
FROM Listings l
INNER JOIN Neighborhoods n on l.neighborhood_id = n.id
INNER JOIN RoomTypes r on l.roomType_id = r.id
GROUP BY n.id;
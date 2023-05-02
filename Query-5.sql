SELECT AVG(l.availability) as "Average Availability", r.roomType
FROM Listings l
INNER JOIN RoomTypes r on l.roomType_id = r.id
GROUP BY l.roomType_id;
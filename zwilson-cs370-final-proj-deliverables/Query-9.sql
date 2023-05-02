SELECT n.name as "Neighborhood Name", r.roomType as "Most Popular Room Type"
FROM Neighborhoods n
INNER JOIN (
  SELECT neighborhood_id, roomType_id, COUNT(*) as roomTypeCount
  FROM Listings
  GROUP BY neighborhood_id, roomType_id
) l ON n.id = l.neighborhood_id
INNER JOIN RoomTypes r ON l.roomType_id = r.id
INNER JOIN (
  SELECT neighborhood_id, MAX(roomTypeCount) as maxRoomTypeCount
  FROM (
    SELECT neighborhood_id, roomType_id, COUNT(*) as roomTypeCount
    FROM Listings
    GROUP BY neighborhood_id, roomType_id
  ) subquery
  GROUP BY neighborhood_id
) subquery2 ON l.neighborhood_id = subquery2.neighborhood_id AND l.roomTypeCount = subquery2.maxRoomTypeCount;
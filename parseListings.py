# Zach Wilson
# Saba Jamalian
# CS 370-03 Final Project
# 5.1.23
#
# This script reads in listings.csv and parses the data to
#        insert it into my proj.db file which was created by
#        my create-db.sql script

#### Imports ####
import csv
import sqlite3




#### Definitions ####
def IndexOfValueInSet(value, theSet):
    if value not in theSet:
        return -1
    setList = list(theSet)
    return setList.index(value)




############ start of logic ############
#### Open CSV ####
file = open("listings.csv", encoding="utf-8")
df = csv.DictReader(file)




##### declare datatypes #####
## lists for table insertion (note: one list per table)
listings = []
hosts = []
neighborhoods = []
roomType = []

#temp sets/lists for data
setOfHostIDs = set()
setOfHostNames = []
setOfNeighborhoods = set()
setOfRoomTypes = set()




#### parse csv ####
for row in df:
    hostAdded = False
    listing_id = None
    name = None
    host_id = None # special logic for seperating into separate table - similar to reviewers logic
    neighborhood_id = None # special logic for seperating into separate table - similar to roomType logic
    latitude = None
    longitude = None
    roomType_id = None # special logic for seperating into separate table - similar to neighborhood logic
    price = None
    minNights = None
    reviewsPerMonth = None
    availability = None
    numReviewsLTM = None
    licenses = None
    for key, value in row.items():
        ## hosts logic
        if key == "host_id":
            host_id = value
            if value not in setOfHostIDs:
                setOfHostIDs.add(value)
                hostAdded = True
        elif key == "host_name":
            if hostAdded:
                setOfHostNames.append(value)
        ## neighborhoods
        elif key == "neighbourhood":
            if value not in setOfNeighborhoods:
                setOfNeighborhoods.add(value)
                neighborhood_id = (len(setOfNeighborhoods) - 1)
            else:
                neighborhood_id = IndexOfValueInSet(value, setOfNeighborhoods)
        ## roomTypes
        elif key == "room_type":
            if value not in setOfRoomTypes:
                setOfRoomTypes.add(value)
                roomType_id = (len(setOfRoomTypes) - 1)
            else:
                roomType_id = IndexOfValueInSet(value, setOfRoomTypes)
        ## all normal data type assignments from here on
        elif key == "id":
            listing_id = value
        elif key == "name":
            name = value
        elif key == "latitude":
            latitude = value
        elif key == "longitude":
            longitude = value
        elif key == "price":
            price = value
        elif key == "minimum_nights":
            minNights = value
        elif key == "reviews_per_month":
            reviewsPerMonth = value
        elif key == "availability_365":
            availability = value
        elif key == "number_of_reviews_ltm":
            numReviewsLTM = value
        elif key == "license":
            licenses = value
    ## append all of the compiled data from the row into necessary lists
    listings.append([listing_id, name, host_id, neighborhood_id, latitude, longitude, roomType_id, price, minNights, reviewsPerMonth, availability, numReviewsLTM, licenses])




#### start the connection to the db ####
# Open a connection to the database
conn = sqlite3.connect('proj.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()




#### inserting into Hosts ####
setOfHostIDs = list(setOfHostIDs)
for index in range(0, len(setOfHostIDs)):
    hosts.append([setOfHostIDs[index], setOfHostNames[index]])
#insert Query for hosts
cursor.executemany('INSERT INTO Hosts VALUES (?, ?)', hosts)




#### inserting into Neighborhoods ####
setOfNeighborhoods = list(setOfNeighborhoods)
for index in range(0, len(setOfNeighborhoods)):
    neighborhoods.append([index, setOfNeighborhoods[index]])
#insert Query for Neighborhoods
cursor.executemany('INSERT INTO Neighborhoods VALUES (?, ?)', neighborhoods)




#### inserting into RoomType ####
setOfRoomTypes = list(setOfRoomTypes)
for index in range(0, len(setOfRoomTypes)):
    roomType.append([index, setOfRoomTypes[index]])
#insert Query for Neighborhoods
cursor.executemany('INSERT INTO RoomTypes VALUES (?, ?)', roomType)




#### inserting into the reviews ####
cursor.executemany('INSERT INTO Listings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', listings)




#### Commit the changes and close the connection ####
conn.commit()
conn.close()




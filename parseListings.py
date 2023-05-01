import csv
import sqlite3

file = open("listings.csv", encoding="utf-8")
df = csv.DictReader(file)

listings = []
hosts = []
neighborhoods = set()
roomType = set()

#temp reviewers data
setOfReviewerIDs = set()
setOfReviewerNames = []

#temp reviews data
reviewsDataRaw = []

#parse csv into
for row in df:
    reviewerAdded = False
    temp = []
    for key, value in row.items():
        if key == "reviewer_id":
            temp.append(value)
            if value not in setOfReviewerIDs:
                setOfReviewerIDs.add(value)
                reviewerAdded = True
        elif key == "reviewer_name" and reviewerAdded:
            setOfReviewerNames.append(value)
        else:
            temp.append(value)
    reviews.append([temp[1],temp[0],temp[3],temp[2],temp[4]])

        
# Open a connection to the database
conn = sqlite3.connect('proj.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

## inserting into the reviewers
setOfReviewerIDs = list(setOfReviewerIDs)
for index in range(0, len(setOfReviewerIDs)):
    reviewers.append([setOfReviewerIDs[index], setOfReviewerNames[index]])
#insert Query
cursor.executemany('INSERT INTO Reviewers VALUES (?, ?)', reviewers)

## inserting into the reviews
cursor.executemany('INSERT INTO Reviews VALUES (?, ?, ?, ?, ?)', reviews)

# Commit the changes and close the connection
conn.commit()
conn.close()




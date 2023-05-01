import csv
import sqlite3

file = open("reviews.csv", encoding="utf-8")
df = csv.DictReader(file)

reviewers = []
reviews = []

#temp reviewers data
setOfReviewerIDs = set()
setOfReviewerNames = []

#temp reviews data
reviewsDataRaw = []

#parse csv into
for row in df:
    reviewerAdded = False
    review_id, listing_id, reviewer_id, datePosted, review
    for key, value in row.items():
        if key == "reviewer_id":
            reviewer_id = value
            if value not in setOfReviewerIDs:
                setOfReviewerIDs.add(value)
                reviewerAdded = True
        elif key == "reviewer_name" and reviewerAdded:
            setOfReviewerNames.append(value)
        elif key == "id":
            review_id = value
        elif key == "listing_id":
            listing_id = value
        elif key == "date":
            datePosted = value
        elif key == "comments":
            review = value
        else:
            print("[Error 01]: Is the open file formatted correctly for this script?")
    reviews.append([review_id, listing_id, reviewer_id, datePosted, review])

        
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
###check reviews
##for index in range(0, 16):
##    print(reviews[index])
cursor.executemany('INSERT INTO Reviews VALUES (?, ?, ?, ?, ?)', reviews)

# Commit the changes and close the connection
conn.commit()
conn.close()




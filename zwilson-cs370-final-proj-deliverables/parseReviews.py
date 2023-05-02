# Zach Wilson
# Saba Jamalian
# CS 370-03 Final Project
# 5.1.23
#
# This script reads in reviews.csv and parses the data to
#        insert it into my proj.db file which was created by
#        my create-db.sql script

#### Imports ####
import csv
import sqlite3




############ start of logic ############
#### Open CSV ####
file = open("reviews.csv", encoding="utf-8")
df = csv.DictReader(file)




##### declare datatypes #####
## lists for table insertion (note: one list per table)
reviewers = []
reviews = []

#temp sets/lists for data
setOfReviewerIDs = set()
setOfReviewerNames = []




#### parse csv ####
for row in df:
    reviewerAdded = False
    review_id = None
    listing_id = None
    reviewer_id = None
    datePosted = None
    review = None
    for key, value in row.items():
        if key == "reviewer_id":
            reviewer_id = value
            if value not in setOfReviewerIDs:
                setOfReviewerIDs.add(value)
                reviewerAdded = True
        elif key == "reviewer_name":
            if reviewerAdded:
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
            print("[Error 01]: " + str(key) + ": " + str(value))
    reviews.append([review_id, listing_id, reviewer_id, datePosted, review])




#### start the connection to the db ####        
# Open a connection to the database
conn = sqlite3.connect('proj.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()




#### inserting into the reviewers ####
setOfReviewerIDs = list(setOfReviewerIDs)
for index in range(0, len(setOfReviewerIDs)):
    reviewers.append([setOfReviewerIDs[index], setOfReviewerNames[index]])
#insert Query
cursor.executemany('INSERT INTO Reviewers VALUES (?, ?)', reviewers)




#### inserting into the reviews ####
cursor.executemany('INSERT INTO Reviews VALUES (?, ?, ?, ?, ?)', reviews)



#### Commit the changes and close the connection ####
conn.commit()
conn.close()




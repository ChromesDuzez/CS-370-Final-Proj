import pandas as pd

data = pd.read_csv("reviews.csv")

columns = []
for line in data:
    columns.append(line)

parsedData = []

counter = 0
for index in data[columns[0]]:
    line = str(index) + ", " + str(data[columns[1]][counter]) + ", " + str(data[columns[2]][counter]) + ", " + str(data[columns[3]][counter]) + ", " + str(data[columns[4]][counter]) + ", " + str(data[columns[5]][counter])
    parsedData.append(line)
    counter += 1

print(parsedData)

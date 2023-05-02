CREATE TABLE Hosts(
	id INT PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE Reviewers(
	id INT PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE Neighborhoods( 
	id INT PRIMARY KEY, 
	name TEXT
);

CREATE TABLE RoomTypes( 
	id INT PRIMARY KEY, 
	roomType TEXT
);

CREATE TABLE Listings( 
	id INT PRIMARY KEY,
	name TEXT,
	host_id INT,
	neighborhood_id INT,
	latitude DECIMAL(8,6),
	longitude DECIMAL(9,6),
	roomType_id INT,
	price DECIMAL(12,2),
	minNights INT,
	reviewsPerMonth DECIMAL(10,2),
	availability INT,
	numReviewsLTM INT,
	licenses TEXT,
	FOREIGN KEY (host_id) REFERENCES Hosts(id),
	FOREIGN KEY (neighborhood_id) REFERENCES Neighborhoods(id),
	FOREIGN KEY (roomType_id) REFERENCES RoomTypes(id)
);

CREATE TABLE Reviews( 
	id INT PRIMARY KEY, 
	listing_id INT,
	reviewer_id INT,
	datePosted Date,
	review TEXT NOT NULL,
	FOREIGN KEY (listing_id) REFERENCES Listings(id),
	FOREIGN KEY (reviewer_id) REFERENCES Reviewers(id)
);
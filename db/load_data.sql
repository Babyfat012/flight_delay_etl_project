LOAD DATA local INFILE 'tmp/dataset/clean_airlines.csv'
INTO TABLE airlines FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA local INFILE 'tmp/dataset/clean_airports.csv'
INTO TABLE airports FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA local INFILE 'tmp/dataset/clean_flights.csv'
INTO TABLE flights FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


CREATE TABLE puzzle (
	PuzzleNum INTEGER,
	Title VARCHAR (255),
	Pieces INTEGER,
	Company VARCHAR (255),
	Puzzle_size VARCHAR,
	PRIMARY KEY (PuzzleNum)
)

COPY puzzle(PuzzleNum, Title, Pieces, Company, Puzzle_size)
FROM 'C:\Misc\Leske_puzzle_list.csv'
DELIMITER ','
CSV HEADER;
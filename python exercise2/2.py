import sqlite3

# Reads the contents of the file and stores it in the list
stephen_king_adaptations_list = []
with open("stephen_king_adaptations.txt", 'r') as file:
    for line in file:
        stephen_king_adaptations_list.append(line.strip())

# Establish a connection to the SQLite database
conn = sqlite3.connect('stephen_king_adaptations.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
             (movieID INTEGER PRIMARY KEY AUTOINCREMENT,
              movieName TEXT,
              movieYear INTEGER,
              imdbRating REAL)''')

# Insert data into a table
for item in stephen_king_adaptations_list:
    movie_id, movie_name, movie_year, imdb_rating = item.split(',')
    c.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
              (movie_name, int(movie_year), float(imdb_rating)))

# Commit the changes and close the connection
conn.commit()
conn.close()

# User interface loop
while True:
    print("Please select the option you want to search for movies：")
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")

    option = input("Please enter the option number：")

    if option == '1':
        movie_name = input("Please enter the name of the movie you want to search：")
        conn = sqlite3.connect('stephen_king_adaptations.db')
        c = conn.cursor()
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
        result = c.fetchone()
        conn.close()

        if result:
            movie_id, movie_name, movie_year, imdb_rating = result
            print("Movie details：")
            print("ID:", movie_id)
            print("Year:", movie_year)
            print("Rating:", imdb_rating)
        else:
            print("The movie could not be found in our database。")

    elif option == '2':
        movie_year = input("Please enter the year of the movie you want to search：")
        conn = sqlite3.connect('stephen_king_adaptations.db')
        c = conn.cursor()
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (int(movie_year),))
        results = c.fetchall()
        conn.close()

        if results:
            print("Movie details：")
            for result in results:
                movie_id, movie_name, movie_year, imdb_rating = result
                print("ID:", movie_id)
                print("Name:", movie_name)
                print("Year:", movie_year)
                print("Rating:", imdb_rating)
        else:
            print("No films from that year can be found in our database。")

    elif option == '3':
        rating = float(input("Please enter the movie rating："))
        conn = sqlite3.connect('stephen_king_adaptations.db')
        c = conn.cursor()
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
        results = c.fetchall()
        conn.close()

        if results:
            print("Movie details：")
            for result in results:
                movie_id, movie_name, movie_year, imdb_rating = result
                print("ID:", movie_id)
                print("Name:", movie_name)
                print("Year:", movie_year)
                print("Rating:", imdb_rating)
        else:
            print("We couldn't find a movie in our database with that rating or higher。")

    elif option == '4':
        break


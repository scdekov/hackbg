import sqlite3
import os
from pprint import pprint


hall = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


def reset_hall():
    hall = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


os.remove("movies.db")
movies = sqlite3.connect("movies.db")
movies.row_factory = sqlite3.Row
cursor = movies.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute("CREATE TABLE IF NOT EXISTS Movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)")
cursor.execute("INSERT INTO Movies(name, rating) VALUES(?, ?)", ("The Hunger Games: Catching Fire", 7.9))
cursor.execute("INSERT INTO Movies(name, rating) VALUES(?, ?)", ("Wreck-It Ralph", 7.8))
cursor.execute("INSERT INTO Movies(name, rating) VALUES(?, ?)", ("Her", 8.3))


cursor.execute('''CREATE TABLE IF NOT EXISTS Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, sdate TEXT, time TEXT,
                    FOREIGN KEY(movie_id) REFERENCES Movies(id))''')
cursor.execute("INSERT INTO Projections(movie_id, type, sdate, time) VALUES(?, ?, ?, ?)", (1, "3D", "2014-04-01", "19:10"))
cursor.execute("INSERT INTO Projections(movie_id, type, sdate, time) VALUES(?, ?, ?, ?)", (1, "2D", "2014-04-01", "19:00"))
cursor.execute("INSERT INTO Projections(movie_id, type, sdate, time) VALUES(?, ?, ?, ?)", (1, "4DX", "2014-04-02", "21:00"))
cursor.execute("INSERT INTO Projections(movie_id, type, sdate, time) VALUES(?, ?, ?, ?)", (3, "2D", "2014-04-05", "20:20"))
cursor.execute("INSERT INTO Projections(movie_id, type, sdate, time) VALUES(?, ?, ?, ?)", (2, "3D", "2014-04-02", "21:00"))
cursor.execute("INSERT INTO Projections(movie_id, type, sdate, time) VALUES(?, ?, ?, ?)", (2, "2D", "2014-04-02", "19:30"))


cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations(id INTEGER PRIMARY KEY, username TEXT,
                    projection_id INTEGER, row INTEGEr, col INTEGER, FOREIGN KEY(projection_id) REFERENCES Projections(id))''')
cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("RadoRado", 1, 2, 1))
cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("RadoRado", 1, 3, 5))
cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("RadoRado", 1, 7, 8))
cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("Ivo", 3, 1, 1))
cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("Ivo", 3, 1, 2))
cursor.execute("INSERT INTO reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("Mysterious", 5, 2, 3))
cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)", ("Mysterious", 5, 2, 4))


def show_movies():
    all_movies = cursor.execute("SELECT * FROM Movies ORDER BY rating DESC").fetchall()
    for movie in all_movies:
        print (movie["id"], movie["name"], movie["rating"])


def show_movie_projections(my_movie_id, my_time=""):
    movie_name = cursor.execute("SELECT name FROM Movies WHERE id = ?", (my_movie_id,))
    print ("Projections for movie " + movie_name.fetchone()[0] + ":")
    if my_time == "":
        proj = cursor.execute("SELECT * FROM Projections WHERE movie_id = ? ORDER BY sdate", (my_movie_id,))
    else:
        proj = cursor.execute("SELECT * FROM Projections WHERE movie_id = ? AND time = ? ORDER BY sdate", (my_movie_id, my_time))
    proj = proj.fetchall()
    for projection in proj:
        available_spots = 100 - len(cursor.execute("SELECT * FROM Reservations WHERE projection_id = ?", (my_movie_id,)).fetchall())
        print (projection["id"], " - ", projection["type"], projection["sdate"], projection["time"], "available spots: ", available_spots)


def print_reservations():
    reservs = cursor.execute("SELECT * FROM Reservations")
    for res in reservs:
        print (res)


def is_in_hall(seat):
    return int(seat["row"][0]) in range(1, 11) and int(seat["col"][0]) in range(1, 11)


def is_avialable(seat):
    return hall[int(seat["row"])][int(seat["col"])] == '.'


def make_reservation():
    client_name = input("Choose name: ")
    number_of_tickets = input("Choose number of tickets: ")
    show_movies()
    choosed_movie_id = input("Choose a movie: ")
    show_movie_projections(choosed_movie_id)
    projection_choose = input("Choose a projection: ")
    un_available_seats = cursor.execute("SELECT col, row FROM Reservations WHERE projection_id = ?", (projection_choose,)).fetchall()
    reset_hall()
    for seat in un_available_seats:
        hall[seat["row"]][seat["col"]] = 'X'
    print("Available seats (marked with a dot):")
    pprint(hall)
    print("")
    seats = []
    while len(seats) != int(number_of_tickets):
        crr_seat = {}
        crr_seat["row"] = input("Choose next seat: ")
        crr_seat["col"] = input("")
        if is_in_hall(crr_seat):
            if is_avialable(crr_seat):
                seats.append(crr_seat)
            else:
                print("This seat is already taken!")
        else:
            print("Lol...NO!")
    movie_name = cursor.execute("SELECT name FROM Movies WHERE id = ?", (choosed_movie_id,)).fetchone()[0]
    date_and_time = cursor.execute("SELECT sdate, time FROM Projections WHERE id = ?", (projection_choose,)).fetchall()
    print("""This is your reservation:
             Movie : {}
             Date and Time : {}
             Seats : ({};{})""".format(movie_name, date_and_time[0]["sdate"], date_and_time[0]["time"], seats[0]["row"]), seats[0]["col"])
    finalize = input("Confirm - type 'finalize':")
    if finalize == "finalize":
        for i in range(number_of_tickets):
            cursor.execute("INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)",
                           (client_name, projection_choose, seats[i]["row"], seats[i]["col"]))


def main():
    make_reservation()
    print_reservations()


if __name__ == '__main__':
    main()

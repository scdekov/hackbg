from Movie import Movie
from Projection import Projection
from Reservation import Reservation
from sqlalchemy.orm import Session
from pprint import pprint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from connection import *




Base.metadata.create_all(engine)
session = Session(bind=engine)


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


class Cinema:

    def __init__(self):
        Base.metadata.create_all(engine)

    def add_movie(self, name, rating):
        session.add(Movie(name=name, rating=rating))
        session.commit()

    def add_projection(self, movie_id, type, data, time):
        session.add(Projection(movie_id=movie_id, type=type, data=data, time=time))
        session.commit()

    def add_reservation(self, username, projection_id, row, col):
        session.add(Reservation(username=username, projection_id=projection_id, row=row, col=col))

    def show_movies(self):
        all_movies = Session.query(Movie).all().order_by(Movie.rating.desc())
        for movie in all_movies:
            print(movie)

    def free_slots_for_projection(self, projection):
        slots = Session.query(Reservation).filter(projection_id == projection)
        free_slots = 100 - len(slots)
        return free_slots

    def show_movie_projections(self, movie_id, date=None):

        if date is None:
            all_projections = Session.query(Projection).all()
            for projection in all_projections:
                print(projection)
        else:
            all_projections = Session.query(Projection).filter(date == date).order_by(Projection.date).all()
            for projection in all_projections:
                free_slots = self.free_slots_for_projection(projection[0])
                print("{} free_slots: {}".format(projection, free_slots))

    def fill_hall_for_projection(self, projection_id):
        unavialable = session.query(Reservation.row, Reservation.col).filter(projection_id == projection_id).all()
        for slot in unavialable:
            hall[slot[0], slot[1]] = 'X'

    def is_position_free(self, position):
        return hall[position[0], position[1]] == '.'

    def make_reservation(self, name, number_of_tickets):
        self.show_movies()
        choosen_movie_id = input("Choose a movie>")
        self.show_movie_projections(choosen_movie_id)
        choosen_projection_id = input("Choose a projection>")
        free_slots_for_choosen_projection = self.free_slots_for_projection(choosen_projection_id)
        if free_slots_for_choosen_projection < number_of_tickets:
            print("Not enought tickets for this projection, only {} available".format(free_slots_for_choosen_projection))
            return
        print("Available seats (marked with a dot):")
        self.reset_hall()
        self.fill_hall_for_projection(choosen_projection_id)
        pprint(hall)
        checked_tickets = 0
        while checked_tickets != number_of_tickets:
            seat = input("Choose seat{}>".format(checked_tickets + 1))
            if self.is_position_free(seat):
                seats = (seat[0], seat[1])
                checked_tickets += 1
            else:
                print("This seat is already taken! or it's outside the hall!")
        choosen_movie_name = session.query(Movie.name).filter(id == choosen_movie_id).one()
        choosen_movie_date = session.query(Movie.date).filter(id == choosen_movie_id).one()
        choosen_movie_time = session.query(Movie.time).filter(id == choosen_movie_id).one()
        choosen_projection_type = session.query(Projection.type).filter(id == choosen_projection_id).one()
        print("This is your reservation:")
        print("Movie: ", choosen_movie_name)
        print("Date and Time: {}:{}  -  ({})".format(choosen_movie_date, choosen_movie_time, choosen_projection_type))
        print("Seats: ", seats)
        is_finalized = input("Confirm - type 'finalize'>")
        if is_finalized == 'finalize':
            for seat in seats:
                session.add(Reservation(username=name, projection_id=choosen_projection_id, row=seat[0], col=seat[1]))
        session.commit()




def main():
    cinema = Cinema()
    cinema.add_movie("The Hunger Games: Catching Fire", 7.8)
    cinema.add_movie("Wreck-It Ralph", 7.9)
    cinema.add_projection(1, "3D", "11.12.2014", "20:10")
    cinema.add_projection(2, "2D", "11.12.2014", "20:00")
    cinema.add_reservation("svetlio", 1, 4, 2)
    cinema.add_reservation("svet", 2, 3, 3)
    cinema.make_reservation("svetlioo", 2)






if __name__ == '__main__':
    main()






















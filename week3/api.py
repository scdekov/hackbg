import requests
import json
from random import shuffle


api = requests.get("https://hackbulgaria.com/api/students/", verify=False)
api_info = api.json()


def list_all_courses():
    courses = []
    for el in api_info:
        for course in el["courses"]:
            if course["name"] not in courses:
                courses.append(course["name"])

    message = "Here are the courses:"
    counter = 0
    for course in courses:
        message += "\n[{}] ".format(counter)
        message += course
        counter += 1

    return message


def match_teams(course_id, team_size, group_time):
    courses = []
    for el in api_info:
        for course in el["courses"]:
            if course["name"] not in courses:
                courses.append(course["name"])
    persons = []
    our_course = courses[course_id]
    for person in api_info:
        for course in person["courses"]:
            if course["name"] == our_course and course["group"] == group_time:
                persons.append(person["name"])
                break
    counter = 0
    shuffle(persons)
    for i in range(len(persons)):
        if counter == team_size:
            print("=" * 20)
            counter = 0
        print (persons[i])
        counter += 1


def main():
    command = input("""Hello, you can use one the following commands:
list_courses - this lists all the courses that are available now.
match_teams <course_id>, <team_size>, <group_time>\n""")
    if command == "list_courses":
        print(list_all_courses())
    else:
        command = command.split(" ")
        try:
            match_teams(int(command[1]), int(command[2]), int(command[3]))
        except IndexError:
            print("WRONG COMMAND!!!")







if __name__ == '__main__':
    main()

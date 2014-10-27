import requests
import json


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
    for i in range(len(persons)):
        if counter == team_size:
            print("=========================")
            counter = 0
        print (persons[i])
        counter += 1


print (list_all_courses())

print (match_teams(4, 2, 2))

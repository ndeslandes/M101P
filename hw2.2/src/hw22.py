#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo

client = pymongo.MongoClient()
students = client.students
grades = students.grades

previous_student = -1
print grades.count()
for grade in grades.find({'type': 'homework'}).sort([('student_id', 1), ('score', 1)]):

    if previous_student != grade['student_id']:
        grades.remove({"_id": grade["_id"]})
    previous_student = grade['student_id']

print grades.count()

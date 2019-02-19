import os
import datetime

Name = raw_input("Please Enter your Name: ")
Age = input("Please Enter your age: ")

DOB = datetime.date.year - Age
Century = DOB + 100

print(Name+" you will turn 100 years in the year "+str(Century))
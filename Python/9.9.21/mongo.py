

import pymongo

class Employee:

    # expects to be instantiated using a dictionary like ...

    def __init__(self, options):
        self._name = options['name']
        self._id = options['id number']
        self._gender = options['gender']
        self._city = options['city']
        self._salary = options['salary']

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id


    def get_gender(self):
        return self._gender


    def get_city(self):
        return self._city


    def get_salary(self):
        return self._salary


    def set_name(self, new_name):
        self._name = new_name

    def set_id(self, new_id):
        self._id = new_id

    def set_gender(self, new_gender):
        self._gender = new_gender

    def set_city(self, new_city):
        self._city = new_city

    def set_salary(self, new_salary):
        self._salary = new_salary


# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type and age of his or her pet.  This data should be stored as the object's attributes.
# Use the object's accessor methods to retrieve the pet's name, type, and age and display this data on the screen.
print("----------------")
print("EMPLOYEE APPLICATION")
print("-----------------")

id = int(input("Please input the id number (e.g. '1,2,3'): "))
name = input("Please input the employee name (e.g. 'Guna'): ")
gender = input("Please input the gender (e.g. 'male'): ")
city = input("Please input the city:")
salary = input("Please enter the salary:")

employee = Employee({'name': name, 'id number': id, 'gender': gender, 'city': city, 'salary': salary})








client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Employees']
information2=mydb.employeeinformation2
# record2={
#     'firstname':'hi',
#     'lastname':'welcome',
#
# }
d={'name': employee._name, 'id number': int(employee._id), 'gender': employee._gender, 'city': employee._city, 'salary':employee._salary}
information2.insert_one(d)
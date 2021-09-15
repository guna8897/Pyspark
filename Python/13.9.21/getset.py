import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Employees']
information2=mydb.employeeinformation2

print("For Search Press 1:")
print("For Update Press 2:")
print("For Delete Press 3:")
print("For insert press 4")
num=int(input("Enter the choice "))
if num==1:
    name=(input("Enter the name"))
    for record in information2.find({"name":name}):
        print(record)
if num==2:
    name=input("Enter the Name")
    salary=int(input("Enter the salary"))
    information2.update_one({"name":name},{"$set":{"salary":salary}})
if num==3:
    name=input("Enter The Name")
    information2.delete_one({"name":name})
if num==4:
    class Employee:

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


    print("EMPLOYEE APPLICATION")

    id = int(input("Please enter the id number : "))
    name = input("Please enter the employee name : ")
    gender = input("Please enter the gender : ")
    city = input("Please enter the city:")
    salary = input("Please enter the salary:")

    employee = Employee({'name': name, 'id number': id, 'gender': gender, 'city': city, 'salary': salary})

    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    mydb = client['Employees']
    information2 = mydb.employeeinformation2

    d = {'name': employee._name, 'id number': int(employee._id), 'gender': employee._gender, 'city': employee._city,
         'salary': employee._salary}
    information2.insert_one(d)


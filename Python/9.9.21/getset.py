import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Employees']
information2=mydb.employeeinformation2
# record2={
#     'firstname':'hi',
#     'lastname':'welcome',
#
# }
print("For Search Press 1:")
print("For Update Press 2:")
print("For Delete Press 3:")
num=int(input("Enter the choice"))
if num==1:
    name=(input("Enter the name"))
    for record in information2.find({"name" :name}):
    # for record in information2.find().sort("name",1):
        print(record)
if num==2:
    name=input("Enter the Name")
    salary=int(input("Enter the salary"))
    information2.update_one({"name":name},{"$set":{"salary":salary}})
if num==3:
    name=input("Enter The Name")
    information2.delete_one({"name":name})
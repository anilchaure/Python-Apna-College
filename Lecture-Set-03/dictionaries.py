student = {
    "name" : "rahul kumar",
    "subjects" : {
        "chem": 35,
        "phy" : 66,
        "math" : 56
    }
}
# print(student)
# print(type(student))
# print(student["subjects"])
# print(student["subjects"]["math"])

#methods in dictionaries
# print(student.keys())
# print(student["subjects"].keys())

#type casting in dictionaries
# print(list(student.keys()))
# print(len(list(student.keys())))
# print(len(student))
student.update({"city": "delhi" })
print(student)
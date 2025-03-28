marks = {
    "Kajal": 100,
    "Prachi": 99,
    "Gunjan": 89,
    0 : "kajal"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Kajal":99, "Babli" : 100})
# print(marks)
print(marks.get("Kajal"))
print(marks["Kajal"]) 

print(marks.get("Kajal2")) # prints None
print(marks["Kajal2"])   # returns an error
studentList = {
    "Park": "Korea",
    "Sam": "USA",
    "Sakura": "Japan"
}

def greeting(name):
    nationality = studentList.get(name)
    if nationality:
        return f"Hi! I'm {name}, and I'm from {nationality}"
    else:
        return "Student not found."

print(greeting("Park"))
print(greeting("Sam"))
print(greeting("Sakura"))

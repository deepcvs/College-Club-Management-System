import random

depts = ['CSE', 'ME', 'ECE', 'CV', 'EEE', 'BT']
sems = ["1", "3", "5", "7"]
isExternal = ["1", "NULL"]
insert_students = open("insert_students.txt", "a")
domains = ['@gmail.com', '@yahoo.com',
           '@hotmail.com', '@rediffmail.com', '@outlook.com']
not_these = [123, 50, 127, 133, 568, 70, 77, 1, 69, 141]

with open("new_insert_students.txt", "a") as f:
    for i in range(700):
        sem = random.choice(sems)
        srn = random.randint(0, 1440)
        cond = srn < 721 and srn not in not_these
        dept = random.choice(depts)
        phone = [str(random.randint(6, 9))] + \
            [str(random.randint(0, 9)) for _ in range(9)]

        string = "INSERT into STUDENT values ("
        string += f"'Student{i}', "
        string += str(round(random.uniform(1, 10), 2)) + ", "
        string += sem + ", "
        if cond:
            string += f"'PES{((random.randint(1319, 3113)) % 2) + 1}UG{18 + int(((7 - int(sem)) / 2))}{dept[:2]}{srn:03}', "
        else:
            string += f"{srn}, "
        string += f"'{dept}', "
        string += f"'Student{i}{random.choice(domains)}', "
        string += "".join(phone)
        if cond:
            string += ", 0);"
        else:
            string += ", " + random.choice(isExternal) + ");"

        f.write(string + "\n")

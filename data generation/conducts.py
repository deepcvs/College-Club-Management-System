import random
events = [i for i in range(10, 50)]

with open("insert_conducts.txt", "a") as f:
    for i in range(40):
        eventid = random.choice(events)
        string = "INSERT into CONDUCTS values (" + \
            str(eventid) + ", " + str(random.randint(1, 9)) + ");"
        events.remove(eventid)
        f.write(string + "\n")

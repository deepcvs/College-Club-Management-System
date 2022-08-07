with open("new.txt", "r") as f:
    with open("new1.txt", "a") as f1:
        j = 0
        for i in f.readlines():
            f1.write(i.replace("NULL", f"'{j:04}'"))
            j += 1

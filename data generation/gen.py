import random
with open("gen.txt", "w") as f:
    for i in range(364):
        f.write(
            f"INSERT into PARTICIPATES_IN values ('{i*2:04}', {random.randint(1, 41)})\n")

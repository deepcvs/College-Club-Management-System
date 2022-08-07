import random
import datetime

start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2023, 1, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

with open("insert_events.txt", "a") as f:
    for i in range(40):
        string = "INSERT into EVENT values (" + \
            str(random.randint(5000, 100000)) + ", "
        string += "NULL, "
        string += f"'Location{random.randint(1319, 3113)}', "
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + \
            datetime.timedelta(days=random_number_of_days)
        string += f"'{str(random_date)}', "
        string += str(i + 10) + ", "
        string += str(random.randint(100, 10000)) + ", "
        string += f"'EVENT{i}');"

        f.write(string + "\n")

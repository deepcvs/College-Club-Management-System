import random

budgets = [
    17514,
    41877,
    78257,
    24256,
    8059,
    55261,
    85500,
    44430,
    68604,
    10986,
    55251,
    45539,
    66369,
    20440,
    24974,
    57231,
    25442,
    85905,
    65564,
    35735,
    18894,
    37410,
    46395,
    21930,
    91105,
    35467,
    69956,
    66410,
    62830,
    97163,
    65179,
    93119,
    84206,
    68264,
    36404,
    80484,
    23020,
    26738,
    33197,
    18861
]

event_id = [
    'EVENT0',
    'EVENT1',
    'EVENT2',
    'EVENT3',
    'EVENT4',
    'EVENT5',
    'EVENT6',
    'EVENT7',
    'EVENT8',
    'EVENT9',
    'EVENT10',
    'EVENT11',
    'EVENT12',
    'EVENT13',
    'EVENT14',
    'EVENT15',
    'EVENT16',
    'EVENT17',
    'EVENT18',
    'EVENT19',
    'EVENT20',
    'EVENT21',
    'EVENT22',
    'EVENT23',
    'EVENT24',
    'EVENT25',
    'EVENT26',
    'EVENT27',
    'EVENT28',
    'EVENT29',
    'EVENT30',
    'EVENT31',
    'EVENT32',
    'EVENT33',
    'EVENT34',
    'EVENT35',
    'EVENT36',
    'EVENT37',
    'EVENT38',
    'EVENT39'
]

print(len(event_id), len(budgets))

with open("new_insert_sponsors_event.txt", "a") as f:
    for i in range(39, -1, -1):
        index = random.randint(0, i)
        f.write(
            f"INSERT into SPONSORS_EVENT values ({budgets[index]}, {random.randint(1, 8)}, {index})\n")
        budgets.pop(index)
        event_id.pop(index)

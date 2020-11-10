import random

jessieDict = {
    "name": "Jessie",
    "spouse": 2,
    "pick": 0,
    "id": 1
}

chrisDict = {
    "name": "Chris",
    "spouse": 1,
    "pick": 0,
    "id": 2
}

elyseDict = {
    "name": "Elyse",
    "spouse": 4,
    "pick": 0,
    "id": 3
}

paulDict = {
    "name": "Paul",
    "spouse": 3,
    "pick": 0,
    "id": 4
}

davidDict = {
    "name": "David",
    "spouse": 6,
    "pick": 0,
    "id": 5
}

kellyDict = {
    "name": "Kelly",
    "spouse": 5,
    "pick": 0,
    "id": 6
}

people = [jessieDict, chrisDict, elyseDict, paulDict, davidDict, kellyDict]
picks = []

while jessieDict.get("pick") == 0 or chrisDict.get("pick") == 0 or elyseDict.get("pick") == 0 or paulDict.get("pick") == 0 or davidDict.get("pick") == 0 or kellyDict.get("pick") == 0:
    current = random.randint(1,6)
    print(people[current].get("name"))
    print(people)
    while people[current].get("pick") == 0:
        trypick = random.randint(1,6)
        print(trypick)
        if( trypick != people[current].get("id") and trypick != people[current].get("spouse")):
            people[current]["pick"] = trypick

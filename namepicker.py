import random

idDict = {
    1: "Jessie",
    2: "Chris",
    3: "Elyse",
    4: "Paul",
    5: "David",
    6: "Kelly"
}

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

picks = []
available = [1,2,3,4,5,6]

while jessieDict.get("pick") == 0:
    pick = random.randint(1,6)
    if pick != jessieDict.get("spouse") and pick != jessieDict.get("id") and pick not in picks:
        jessieDict["pick"] = pick
        picks.append(pick)
        available.remove(pick)
        break
    if len(available) < 3 and jessieDict.get("id") in available and jessieDict.get("spouse") in available:
        print("Bad outcome - try again")
        break
    if len(available) < 2 and jessieDict.get("id") in available:
        print("Bad outcome - try again")
        break

while chrisDict.get("pick") == 0:
    pick = random.randint(1,6)
    if pick != chrisDict.get("spouse") and pick != chrisDict.get("id") and pick not in picks:
        chrisDict["pick"] = pick
        picks.append(pick)
        available.remove(pick)
        break
    if len(available) < 3 and chrisDict.get("id") in available and chrisDict.get("spouse") in available:
        print("Bad outcome - try again")
        break
    if len(available) < 2 and chrisDict.get("id") in available:
        print("Bad outcome - try again")
        break

while elyseDict.get("pick") == 0:
    pick = random.randint(1,6)
    if pick != elyseDict.get("spouse") and pick != elyseDict.get("id") and pick not in picks:
        elyseDict["pick"] = pick
        picks.append(pick)
        available.remove(pick)
        break
    if len(available) < 3 and elyseDict.get("id") in available and elyseDict.get("spouse") in available:
        print("Bad outcome - try again")
        break
    if len(available) < 2 and elyseDict.get("id") in available:
        print("Bad outcome - try again")
        break

while paulDict.get("pick") == 0:
    pick = random.randint(1,6)
    if pick != paulDict.get("spouse") and pick != paulDict.get("id") and pick not in picks:
        paulDict["pick"] = pick
        picks.append(pick)
        available.remove(pick)
        break
    if len(available) < 3 and paulDict.get("id") in available and paulDict.get("spouse") in available:
        print("Bad outcome - try again")
        break
    if len(available) < 2 and paulDict.get("id") in available:
        print("Bad outcome - try again")
        break

while davidDict.get("pick") == 0:
    pick = random.randint(1,6)
    if pick != davidDict.get("spouse") and pick != davidDict.get("id") and pick not in picks:
        davidDict["pick"] = pick
        picks.append(pick)
        available.remove(pick)
        break
    if len(available) < 3 and davidDict.get("id") in available and davidDict.get("spouse") in available:
        print("Bad outcome - try again")
        break
    if len(available) < 2 and davidDict.get("id") in available:
        print("Bad outcome - try again")
        break

while kellyDict.get("pick") == 0:
    pick = random.randint(1,6)
    if pick != kellyDict.get("spouse") and pick != kellyDict.get("id") and pick not in picks:
        kellyDict["pick"] = pick
        picks.append(pick)
        available.remove(pick)
        break
    if len(available) < 3 and kellyDict.get("id") in available and kellyDict.get("spouse") in available:
        print("Bad outcome - try again")
        break
    if len(available) < 2 and kellyDict.get("id") in available:
        print("Bad outcome - try again")
        break

print(f"Jessie's pick is: {idDict.get(jessieDict.get('pick'))}")
print(f"Chris's pick is: {idDict.get(chrisDict.get('pick'))}")
print(f"Elyse's pick is: {idDict.get(elyseDict.get('pick'))}")
print(f"Paul's pick is: {idDict.get(paulDict.get('pick'))}")
print(f"David's pick is: {idDict.get(davidDict.get('pick'))}")
print(f"Kelly's pick is: {idDict.get(kellyDict.get('pick'))}")

backpack_1 = {
    "first aid kit": 1,
    "lighter": 2,
    "sunglasses": 1,
    "trousers": 2,
    "hygienic set": 1,
    "flashlight": 1,
    "footwear": 2,
    "socks": 3,
    "sleeping bag": 1,
    "water jacket": 1,
    "cap": 1,
    "dishes": 2,
    "woolen gloves": 1,
    "tent": 1
}

backpack_2 = {
    "first aid kit": 1,
    "lighter": 2,
    "sunglasses": 1,
    "trousers": 2,
    "hygienic set": 1,
    "flashlight": 1,
    "footwear": 2,
    "socks": 3,
    "sleeping bag": 1,
    "batteries": 4,
    "poncho": 1,
    "t-shirts": 3
}

common_keys = backpack_1.keys() & backpack_2.keys()
only_first = backpack_1.keys() - backpack_2.keys()
only_second = backpack_2.keys() - backpack_1.keys()

print("In both:")
for item in common_keys:
    print(item, backpack_1[item])

print()

print("Only in the first:")
for item in only_first:
    print(item, backpack_1[item])

print()

print("Only in the other:")
for item in only_second:
    print(item, backpack_2[item])
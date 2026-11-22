products = {
    1: ["Core-i3-4330", 9, 4500],
    2: ["Core i5-4670K", 3, 8500],
    3: ["AMD FX-6300", 6, 3700],
    4: ["Pentium G3220", 8, 2100],
    5: ["Core i5-3450", 5, 6400]
}

for key in sorted(products):
    item = products[key]
    print(key, item[0], item[1], item[2])

while True:
    command = int(input())
    
    if command == 0:
        break
    
    product_id = command
    
    if product_id in products:
        new_quantity = int(input())
        products[product_id][1] = new_quantity
    else:
        print("product missing")


for key in sorted(products):
    item = products[key]
    print(key, item[0], item[1], item[2])
city_to_country = {}

n = int(input())

for a in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    
    for city in cities:
        city_to_country[city] = country

m = int(input())
queries = []

for a in range(m):
    city_name = input().strip()
    queries.append(city_name)

for city_name in queries:
    print(city_to_country[city_name])
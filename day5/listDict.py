travel_log = [ 
    {"country": "france",
     "visits": 12,
     "cities":["paris", "lille","dijon"]
     },
     {"country": "spain",
      "visits": 5,
      "cities":["madrid", "barcelona"]
    },
]
# country = input("input country name: ")
# visits = int(input("num of visits: "))
# cities = input("list of cities: ").split(",") 
def add_new_country(country,visits,cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)
add_new_country("russia",2,["moscow","sxsss"])
print(travel_log)
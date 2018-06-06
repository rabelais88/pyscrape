import random

genrnd = lambda min, max: str(random.randint(min, max))
print('rank,city,population')
cities = ['shanghai', 'karachi', 'beijing', 'shenzhen', 'tianjin']

for idx, city in enumerate(cities):
  print(','.join([str(idx), city, genrnd(100, 20000)]))

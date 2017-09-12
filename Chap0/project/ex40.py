# encoding: utf-8
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention! 把方法放入字典中，事件驱动引擎的基础
cities['_find'] = find_city

while True:
    print ("State? (ENTER to quit)",)
    state = input("> ")
    if not state: break

    # this line is the most important ever!study!
    city_found = cities['_find'](cities, state)
    print (city_found)

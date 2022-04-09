
#Day Trip Generator

# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment
# if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


destinations = ['Tokyo', 'Osaka', 'Kyoto', 'Sendai', 'Gunma', 'Hokkaido']
transportations = ['high-speed train', 'local train', 'plane', 'car', 'Mario Go-Kart']
entertainments = ['visiting a temple', 'going to a cat cafe', 'going to a game center', 'participating in a tea ceremony', 'climbing a mountain']
restaurants = ['MOS Burger', 'Inari Steak', 'Coco Curry Ichibanya', 'Hamazushi', '7-11']

import random

def select_random_destination():
    random_destination_input = 'n'
    print('Welcome to Japan! If you are not sure what you want to do for vacation, no worries.')
    destination_max = len(destinations) - 1
    while random_destination_input == 'n':
        destination_index = random.randint(0, destination_max)
        destination = destinations[destination_index]
        random_destination_input = input(f'We have selected {destination} for your destination. Does this sound good? Enter y/n: ')
    print('Great, glad that is decided. Moving on.')

select_random_destination()

print('')

def select_random_transportation():
    random_transportation_input = 'n'
    transportation_max = len(transportations) - 1
    while random_transportation_input == 'n':
        transportation_index = random.randint(0, transportation_max)
        transportation = transportations[transportation_index]
        random_transportation_input = input(f'We have selected {transportation} as your mode of transportation. Does this sound good? Enter y/n: ')
    print('Great, glad that is decided. Moving on.')
    
select_random_transportation()

print('')

def select_random_entertainment():
    random_entertainment_input = 'n'
    entertainment_max = len(entertainments) - 1
    while random_entertainment_input == 'n':
        entertainment_index = random.randint(0, entertainment_max)
        entertainment = entertainments[entertainment_index]
        random_entertainment_input = input(f'We have selected {entertainment} for you to do this afternoon. Does this sound good? Enter y/n: ')
    print('Great, that is a lovely choice. Moving on.')

select_random_entertainment()

print('')

def select_random_restaurant():
    random_restaurant_input = 'n'
    restaurant_max = len(restaurants) - 1
    while random_restaurant_input == 'n':
        restaurant_index = random.randint(0, restaurant_max)
        restaurant = restaurants[restaurant_index]
        random_restaurant_input = input(f'We have selected {restaurant} for as your dining option. Does this sound good? Enter y/n: ')
    print('Great, that is some yummy food. Moving on.')

select_random_restaurant()
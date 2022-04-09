
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
final_destination = 'n'

def select_random_destination(final_destination):
    print('Welcome to Japan! If you are not sure what you want to do for vacation, no worries.')
    destination_max = len(destinations) - 1
    while final_destination == 'n':
        destination_index = random.randint(0, destination_max)
        destination = destinations[destination_index]
        final_destination = input(f'We have selected {destination} for your destination. Does this sound good? Enter y/n: ')
    print('Great, glad that is decided. Moving on.')

select_random_destination(final_destination)

print('')
final_transportation = 'n'

def select_random_transportation(final_transportation):
    transportation_max = len(transportations) - 1
    while final_transportation == 'n':
        transportation_index = random.randint(0, transportation_max)
        transportation = transportations[transportation_index]
        final_transportation = input(f'We have selected {transportation} as your mode of transportation. Does this sound good? Enter y/n: ')
    print('Great, glad that is decided. Moving on.')
    
select_random_transportation(final_transportation)

print('')
final_entertainment = 'n'

def select_random_entertainment(final_entertainment):
    entertainment_max = len(entertainments) - 1
    while final_entertainment == 'n':
        entertainment_index = random.randint(0, entertainment_max)
        entertainment = entertainments[entertainment_index]
        final_entertainment = input(f'We have selected {entertainment} for you to do this afternoon. Does this sound good? Enter y/n: ')
    print('Great, that is a lovely choice. Moving on.')

select_random_entertainment(final_entertainment)

print('')
final_restaurant = 'n'

def select_random_restaurant(final_restaurant):
    restaurant_max = len(restaurants) - 1
    while final_restaurant == 'n':
        restaurant_index = random.randint(0, restaurant_max)
        restaurant = restaurants[restaurant_index]
        final_restaurant = input(f'We have selected {restaurant} for as your dining option. Does this sound good? Enter y/n: ')
    print('Great, that is some yummy food. Moving on.')

select_random_restaurant(final_restaurant)

print('')
print('Congrats! Your random Japan trip has been decided. Please just make sure that this is what you wanted.')
print('Your trip looks like: ')

# def create_trip():

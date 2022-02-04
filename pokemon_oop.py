import requests
import pprint

class Type:
    def __init__(self):
        self

class Character:
    pokemon = []
    def __init__(self, name, height, weight, hp, attack, defense, speed):
        self.name = name
        self.height = height
        self.weight = weight
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def __repr__(self):
        return f'{self.name}'

water = f"https://pokeapi.co/api/v2/type/water/"
grass = f"https://pokeapi.co/api/v2/type/grass/"
fire = f"https://pokeapi.co/api/v2/type/fire/"
rock = f"https://pokeapi.co/api/v2/type/rock/"
electric = f"https://pokeapi.co/api/v2/type/electric/"

def get_fire():
    chosen_fire = requests.get(fire).json()["pokemon"]
    print (f'\nFire characters are:')
    for i in range (50):
        print (f'{chosen_fire[i]["pokemon"]["name"]}, ', end= "")
def get_water():
    print (f'\nWater characters are:')
    chosen_water = requests.get(water).json()["pokemon"]
    for i in range (100):
        print (f'{chosen_water[i]["pokemon"]["name"]}, ', end= " ")
def get_grass():  
    print (f'\nGrass characters are:')
    chosen_grass = requests.get(grass).json()["pokemon"]
    for i in range (100):
        print (f'{chosen_grass[i]["pokemon"]["name"]}, ', end= " ")
def get_rock():
    print (f'\nRock characters are:')
    chosen_rock = requests.get(rock).json()["pokemon"]
    for i in range (50):
        print (f'{chosen_rock[i]["pokemon"]["name"]}, ', end= " ")
def get_electric():
    print (f'\nElectric characters are:')
    chosen_electric = requests.get(electric).json()["pokemon"]
    for i in range (50):
        print (f'{chosen_electric[i]["pokemon"]["name"]}, ', end= " ")


def choose_char():
    character = input('\n\nEnter the character to see its stats and add it to your collection: >').lower()
    ch_name = character.title()
    api_link = f"https://pokeapi.co/api/v2/pokemon/{character}/"
    h = requests.get(api_link).json()["height"]
    w = requests.get(api_link).json()["weight"]
    hitp = requests.get(api_link).json()["stats"][0]['base_stat']
    atk = requests.get(api_link).json()["stats"][1]['base_stat']
    de = requests.get(api_link).json()["stats"][2]['base_stat']
    spd = requests.get(api_link).json()["stats"][5]['base_stat']
    ability1 = requests.get(api_link).json()["abilities"][0]["ability"]["name"]
    ability2 = requests.get(api_link).json()["abilities"][1]["ability"]["name"]

    att_dict = {"name" : ch_name,
                "height" : h,
                "weight" : w,
                "hp" : hitp,
                "attack" : atk,
                "defense" : de,
                "speed" : spd,
                "abilities": [ability1, ability2]
                }
    new_addition = Character(ch_name, h, w, hitp, atk, de, spd)
    Character.pokemon.append(new_addition)   

    print (att_dict)


game = True
while game == True:
    print (f'\nWelcome to the Pokemon Data Center. We feature five types of Pokemon.\n They are Water, Grass, Fire, Rock, and Elecric.')
    flag = True
    while flag == True:
        user_type = input("\nEnter a type to see characters of that type or enter 'skip' to go straight to character selection. >").lower()
        if user_type == 'water':
            get_water()
            flag = False
        elif user_type == 'grass':
            get_grass()
            flag = False
        elif user_type == 'fire':
            get_fire()
            flag = False
        elif user_type == 'rock':
            get_rock()
            flag = False
        elif user_type == 'electric':
            get_electric()
            flag = False
        elif user_type == 'skip':
            flag = False
        else:
            print("Please enter a valid selection.")

    choose_char()
    print (f'Your collection is now: {Character.pokemon}')


    while True:
        cont = input("\nWould you like to make another selection? (y/n) >").lower()
        if cont == 'y':
            break
        elif cont == 'n':
            game = False
            break
        else:
            continue
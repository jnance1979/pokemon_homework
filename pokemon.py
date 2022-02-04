import requests
import pprint   

water = f"https://pokeapi.co/api/v2/type/water/"
grass = f"https://pokeapi.co/api/v2/type/grass/"
fire = f"https://pokeapi.co/api/v2/type/fire/"
rock = f"https://pokeapi.co/api/v2/type/rock/"
electric = f"https://pokeapi.co/api/v2/type/electric/"

def get_fire():
    chosen_fire = requests.get(fire).json()["pokemon"]
    print (f'\nFire characters are:')
    for i in range (88):
        print (f'{chosen_fire[i]["pokemon"]["name"]}, ', end= "")
def get_water():
    print (f'\nWater characters are:')
    chosen_water = requests.get(water).json()["pokemon"]
    for i in range (162):
        print (f'{chosen_water[i]["pokemon"]["name"]}, ', end= " ")
def get_grass():  
    print (f'\nGrass characters are:')
    chosen_grass = requests.get(grass).json()["pokemon"]
    for i in range (124):
        print (f'{chosen_grass[i]["pokemon"]["name"]}, ', end= " ")
def get_rock():
    print (f'\nRock characters are:')
    chosen_rock = requests.get(rock).json()["pokemon"]
    for i in range (89):
        print (f'{chosen_rock[i]["pokemon"]["name"]}, ', end= " ")
def get_electric():
    print (f'\nElectric characters are:')
    chosen_electric = requests.get(electric).json()["pokemon"]
    for i in range (89):
        print (f'{chosen_electric[i]["pokemon"]["name"]}, ', end= " ")


def choose_char():
    character = input('\n\nEnter the character to see his/her/its stats: >').lower()
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
    print (att_dict)

game = True
while game == True:
    print (f'Welcome to the Pokemon data center. We feature five types of Pokemon.\n They are Water, Grass, Fire, Rock, and Elecric.')
    flag = True
    while flag == True:
        user_type = input("\nEnter a type to see all characters of that type or enter 'skip' to go straight to character selection. >").lower()
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

    while True:
        cont = input("\nWould you like to make another selection? (y/n) >").lower()
        if cont == 'y':
            break
        elif cont == 'n':
            game = False
            break
        else:
            continue
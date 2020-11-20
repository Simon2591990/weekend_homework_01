# WRITE YOUR FUNCTIONS HERE
import pdb
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, sale):
    shop["admin"]["total_cash"] += sale

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, pets_sold):
    shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    list_of_specified_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            list_of_specified_breed.append(pet["name"])
    return list_of_specified_breed

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
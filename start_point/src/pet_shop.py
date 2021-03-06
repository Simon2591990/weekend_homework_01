# WRITE YOUR FUNCTIONS HERE
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
                
def remove_pet_by_name(shop, name):
    pet_index = -1
    for pet in shop["pets"]:
        pet_index += 1
        if pet["name"] == name:
            shop["pets"].pop(pet_index)

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer,  pet):
    if customer["cash"] >= pet["price"]:
            return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
     if pet != None:
         if customer_can_afford_pet(customer, pet):

            add_pet_to_customer(customer, pet["name"])
            remove_pet_by_name(shop, pet["name"])
            remove_customer_cash(customer, pet["price"])
            add_or_remove_cash(shop, pet["price"])
            increase_pets_sold(shop, 1)
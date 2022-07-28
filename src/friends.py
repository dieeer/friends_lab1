def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    # first thing, get person and navigate through dict until favourites
    # second, we need to navigate within dict favourites and fetch snacks
    # snacks is list
    # need to check if food is in snacks list
    snacks = person["favourites"]["snacks"]
    if food in snacks: 
        return True
    else:
        return False
    
def add_friend(person, friend):
    # first to get list of friends of person 
    list_of_friends = person["friends"]
    list_of_friends.append(friend)
    # append friend to list that received 

def remove_friend(person, friend):
    # first to get list of friends of person 
    list_of_friends = person["friends"]
    list_of_friends.remove(friend)

def total_money(persons):
    # init total monies with 0 value 
    total_monies = 0 
    #  iterate each person in list
    for person in persons:
        total_monies += person["monies"]
    return total_monies
        # inside loop get value of monies of current person 
        #add value to total monies  

def lend_money(lender, borrower, amount):
    # took value of money 
    lender["monies"] -= amount 
    borrower["monies"] += amount 
    # minusses amount from lender 
    # adding to borrower 

def all_favourite_foods(persons):
    # init empty list to hold result 
    total_favourites = []
    # iterate through each person 
    for person in persons:
        snacks = person["favourites"]["snacks"]
        for snack in snacks: 
            total_favourites.append(snack)
    return total_favourites 

def find_no_friends(persons):
    sad_people = []
    for person in persons:
        if len(person["friends"]) == 0:
            sad_people.append(person)
    return sad_people

def unique_favourite_tv_shows(persons):
    tv_shows = []
    for person in persons:
        if not person["favourites"]["tv_show"] in tv_shows:
            tv_shows.append(person["favourites"]["tv_show"])


    return tv_shows


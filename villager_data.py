# line added to test git command line execution
"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    # TODO: replace this with your code
    file = open(filename)
    species_list = []
    for data in file:
        entry = data.split("|")
        species_name = entry[1]
        species_list.append(species_name)

    species = set(species_list) 

    return species
    

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    # TODO: replace this with your code
    file = open(filename)
    villagers = []
    for data in file:
        entry = data.split("|")
        if search_string == entry[1]:
            villagers.append(entry[0])
        elif search_string == "All":
            villagers.append(entry[0])

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    file = open(filename)

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    for data in file:
        entry = data.split("|")
        hobby = entry[3]
        name = entry[0]
        
        if hobby == 'Fitness':
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    return [ 
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]
            
        


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    file = open(filename)
    tuple_list = []

    for data in file:
        entry = data.split("|")
        tuple = set(entry)
        tuple_list.append(tuple)
    
    return tuple_list 


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    file = open(filename)

    for data in file:
        entry = data.split("|")
        if entry[0] == villager_name:
            print(entry[4])   
        elif entry[0] != villager_name:
            print(f'This villager does not exist!')
            return None 

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    file = open(filename)
    personality = []
    likeminded = set()

    for data in file:
        entry = data.split("|")
        if entry[0] == villager_name:
            personality.append(entry[2])
            
            for i in range(len(data)): 
                if i < 4 and entry[2] in personality:
                    likeminded.add(entry[0])
                    
    
    return likeminded







#print(all_species("villagers.csv"))
#print(get_villagers_by_species("villagers.csv", 'Dog'))
print(all_names_by_hobby("villagers.csv"))  
#print(all_data('villagers.csv')) 
#print(find_motto('villagers.csv', 'Ismarji'))
#print(find_likeminded_villagers('villagers.csv', 'Curt'))
from controllers.request import getCategories


def print_mainMenu():
    s = "-"*30
    print(s)
    print("Command Menu")
    print(s)
    print ('1 - List all Categories')
    print ('2 - List all Meals by Category')
    print ('3 - Search Meal by Name')
    print ('4 - Random Meal')
    print ('5 - List all Areas')
    print ('6 - List all Meals by Area')
    print ("7 - Menu")
    print ('0 - Exit' )


### import Request
def opt1():
    s = '-'*30
    print("{}\nList all categories\n{}".format(s,s))
    #categories = Request.get_Categories()
    categories = getCategories()
    for category in categories:
        print(category)
    print(s)


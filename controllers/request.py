import requests
from models.category import Category
# from models.meal import Meal
# from models.recipe import Recipe


 
# API base URL
BASE_URL = "https://www.themealdb.com/api/json/v1/1/"

def getCategories():
  """
  Get all meal categories from themealdb
  """
  url = f'{BASE_URL}/categories.php'
  r = requests.get(url)
  categories = []

  if r.status_code == 200:
    json = r.json()
    #print(json['categories'])
    for c in json['categories']:
      #print(c['idCategory'],c['strCategory'],c['strCategoryDescription'])
      category = Category(c['idCategory'],c['strCategory'],c['strCategoryDescription'])
      categories.append(category)

  else:
    print("error")
  return categories


# def get_Areas():
#     """get all Areas from themealddb
#     """
#     url = 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
#     r = requests.get(url)

#     areas = []

#     if r.status_code == 200:
#        for m in r.json()['meals']:
#         area = m['strArea']
#         areas.append(area)
#         #print("{} - {}".format(cat['idCategory'], cat['strCategory'])) 
        
    
#     else:
#         print('An error has ocurred')

#     return areas

# def get_MealsBy(category):
#     url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c='+ category
#     r = requests.get(url)

#     meals = []

#     if r.status_code == 200:
#        for m in r.json()['meals']:
#         meal = Meal(m['idMeal'],m['strMeal'])
#         meals.append(meal)
#         #print("{} - {}".format(cat['idCategory'], cat['strCategory'])) 
        
    
#     else:
#         print('An error has ocurred')

#     return meals

# def get_MealByName(name):
#     url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + name
#     r = requests.get(url)
#     if r.status_code == 200:
#         m = r.json()['meals']
#         i = 1
#         ingredients = []
#         measures = []
#         while  m[0][f'strIngredient{i}'] != '':
#             ingredients.append(m[0][f'strIngredient{i}'])
#             measures.append(m[0][f'strMeasure{i}'])
#             i += 1
        
#         instructions = m[0]['strInstructions']
#         meal = m[0]['strMeal']
#         id = m[0]['idMeal']
#         recipe = Recipe(id, meal, instructions, ingredients, measures)
#     else:
#        print('An error has ocurred') 
#     return recipe

# def get_MealByRamdom():
#     url = 'https://www.themealdb.com/api/json/v1/1/random.php' 
#     r = requests.get(url)
#     if r.status_code == 200:
#         m = r.json()['meals']
#         i = 1
#         ingredients = []
#         measures = []
#         while  m[0][f'strIngredient{i}'] != '':
#             ingredients.append(m[0][f'strIngredient{i}'])
#             measures.append(m[0][f'strMeasure{i}'])
#             i += 1
        
#         instructions = m[0]['strInstructions']
#         meal = m[0]['strMeal']
#         id = m[0]['idMeal']
#         recipe = Recipe(id, meal, instructions, ingredients, measures)
#     else:
#        print('An error has ocurred') 
#     return recipe

# def get_MealsByArea(area):
#     url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a='+ area
#     r = requests.get(url)

#     meals = []

#     if r.status_code == 200:
#        for m in r.json()['meals']:
#         meal = Meal(m['idMeal'],m['strMeal'])
#         meals.append(meal)
#         #print("{} - {}".format(cat['idCategory'], cat['strCategory'])) 
        
    
#     else:
#         print('An error has ocurred')

#     return meals



if __name__ == "__main__":
    categories = getCategories()
    for c in categories:
       print(c)
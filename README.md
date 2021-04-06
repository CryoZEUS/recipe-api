
# recipe-api


![GitHub last commit](https://img.shields.io/github/last-commit/cryozeus/recipe-api?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/cryozeus/recipe-api?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/cryozeus/recipe-api?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/cryozeus/recipe-api?style=for-the-badge)

### An Application that creates, manages recipes for restaurants and delivers custom results


## Recipe:
Recipe of menu items like Chicken Biryani, Pasta, Pizza, etc.

## Ingredients:
What ingredients need to be used to create a recipe? It can either be an SKU or a sub-recipe, which itself is a recipe. It’ll have quantity, unit, and cost.

## SKU:
A raw stock keeping unit (SKU) like Onion, Tomato, etc. It’ll have a name, cost, and unit.  
On every create/update of a recipe an async task needs to be triggered that will calculate the cost of each ingredient and total cost of the recipe.  
Design table schema for the recipe, SKU, and ingredient from your understanding.


Example:

### Recipe: BUTTER GARLIC PRAWNS

### Ingredients: 

- CHUNKY GARLIC OIL (Recipe) (10 – gm)  
- MARINATED PRAWNS (Recipe) (137 – gm)  
- Cherry Tomato (SKU) (5 – gm)  
- Black Olives (SKU) (25 – gm)  
- Parsley (SKU) (1 – gm)  
- Butter salted (SKU) (5 – gm)  
- Chilli flakes (SKU) (1 – gm)  
- Salt (SKU) (1 – gm)  
- Lemon (SKU) (10 – gm)  

### Recipe Output:  

1 – Portion  

The above recipe “BUTTER GARLIC PRAWNS” has ingredients that have name, type, quantity, and unit respectively.   
It has two recipes which are sub-recipes – “CHUNKY GARLIC OIL” and “MARINATED PRAWNS”, these recipes will have another set of ingredients, and recipe output which needs to be in same units as used in main recipe. For e.g. CHUNKY GARLIC OIL recipe output will be in kg or gm equivalent, such that ‘gm’ can be used in “BUTTER GARLIC PRAWNS”.  

Here cost of SKUs will be taken directly from the SKU model with respect to quantities but recipes need to be flattened on the SKU level and the cost of the recipe will be calculated from there and calculated according to the quantity of each ingredient.  

Recipe output is basically how much “BUTTER GARLIC PRAWNS” is created after using these ingredients, It can be 10 kg, 2 Portion, etc.  

## Required APIs:

- List API for recipes that will contain names of recipes, total cost, number of ingredients. Users can order by using any of these fields.  
- API to create a recipe.  
- API to Update a recipe.  
- Detail API for a recipe, Where users can see details of each ingredient.  
- Delete API for a recipe.  
- List API for SKU.  
- API to create an SKU.  
- API to Update an SKU.  
- Provide a postman collection also for all APIs.  

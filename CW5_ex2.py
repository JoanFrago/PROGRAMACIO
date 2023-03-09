def cakes(recipe, ingredients):
    minimo = []
    for elem in recipe:
        if elem in ingredients:
            if ingredients[elem]//recipe[elem] >= 1:
                minimo.append(ingredients[elem]//recipe[elem])
        else:
            print("0")
            break
    if not minimo==[]:
        print(min(minimo))
    
cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, 'milk': 200})
cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})
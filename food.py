pasta = ("pasta Arabiata", "italian", 20,"medium")
biriyani = ("chicken biriyani", "indian", 45,"hard")
print("recipe 1:", pasta)
print("name:",pasta[0]) 
print("cuisine:",pasta[1])
print ("difficulty:",pasta[-1])

all_recipes = (pasta, biriyani)
print("\nFrist recipe name:", all_recipes[0][0])
print("Second recipe name:", all_recipes[1][2], "min")
print("pasta details (sliced):", pasta[1:3])

print("\npasta recipe details:")
for detail in pasta:
    print( "-",detail)

    pasta_ingredients = {"tomato", "garlic", "olive oil", "chili", "pasta", "garlic"}
    biriyani_ingredients = {"chicken", "rice", "onion", "spices", "garlic","tomato"}
    print("\nPasta ingredients:", pasta_ingredients)
    print("Biriyani ingredients:", biriyani_ingredients) 
    print("Total pasta ingredients:",len(pasta_ingredients))

    pasta_ingredients.add("parmasan")
    pasta_ingredients.discard("chili")
    print("\nUpdated pasta ingredients:", pasta_ingredients)

    all_ingredients = pasta_ingredients.union(biriyani_ingredients)
    common = pasta_ingredients.intersection(biriyani_ingredients)
    only_pasta = pasta_ingredients.difference(biriyani_ingredients)
    unique_to_each = pasta_ingredients.symmetric_difference(biriyani_ingredients)

    print("\nAll ingredients:", all_ingredients)
    print("Common ingredients:", common)
    print("Ingredients only in pasta:", only_pasta)
    print("Ingredients unique to each:", unique_to_each)
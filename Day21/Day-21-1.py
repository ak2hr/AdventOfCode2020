import copy

allAllergens = set()
allIngredients = set()
ingredientLists = []
allergenLists = []

def main():
    file = open("Day21/input.txt", "r")
    for line in file:
        line = line.strip()
        ingredients = line[:line.find('(') - 1].split(' ')
        allergens = line[line.find("contains") + 9:line.find(')')].split(", ")
        for ingredient in ingredients:
            allIngredients.add(ingredient)
        for allergen in allergens:
            allAllergens.add(allergen)
        ingredientLists.append(ingredients)
        allergenLists.append(allergens)
    
    unsolvedAllergens = copy.copy(allAllergens)
    containsAllergens = set()
    while(len(unsolvedAllergens) > 0):
        toBeRemoved = {}
        for allergen in unsolvedAllergens:
            contained = []
            for x in range(len(ingredientLists)):
                if(allergen in allergenLists[x]):
                    contained.append(ingredientLists[x])
            intersected = list(set(contained[0]).intersection(*contained))
            if(len(intersected) == 1):
                toBeRemoved[allergen] = intersected[0]
        for allergen in toBeRemoved:
            unsolvedAllergens.remove(allergen)
            for ingredientList in ingredientLists:
                if(toBeRemoved[allergen] in ingredientList):
                    ingredientList.remove(toBeRemoved[allergen])
    total = 0
    for ingredientList in ingredientLists:
        total += len(ingredientList)
    print(total)

    
if __name__ == '__main__':
    main()
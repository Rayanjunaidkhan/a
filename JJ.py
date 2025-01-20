weshi = 800
tortilla_wrap = 950
nugg_wrap = 650
lemonade = 250
small_meal = 200
large_meal = 300

option1 = str(input("weshi burger(Y/N): ")).capitalize()
option2 = str(input("tortilla_wrap(Y/N): ")).capitalize()
option3 = str(input("nugg_wrap(Y/N): ")).capitalize()

if(option1 == "Y" or option2 == "Y" or option3 == "Y") :
    sauce = int(input("which sauce would you like 1. Atomic  2.Garlic 3. Greek 4. Chipotle 5. Mushroom :: "))
    size = str(input("Do you want it with a meal(Y/N): ")).capitalize()
    if(size == "Y"):
        size_1 = str(input("What size should the meal be(L:large//S:small): ")).capitalize()
        if (size_1 == "S"):
            size2 = small_meal 
            meal_cost = 200
        elif(size_1 == "L"):
            size2 = large_meal 
            meal_cost = 300
if(option1 == "Y"):
    costweshi = weshi
if(option2 == "Y"):
    costtortilla = tortilla_wrap
if (option3 == "Y"):
    cost_nugg = nugg_wrap

method = str(input("Will you pay by cash or card: ")).lower()
if(method == "cash"):
    taxper = 0.16
elif(method == "card"):
    taxper = 0.05

finalcost = costweshi + costtortilla + cost_nugg + meal_cost
# for tax
tax = finalcost * taxper
print(finalcost + tax)
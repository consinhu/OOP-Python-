# Define tuple called ingredients
ingredients = ("flour", "butter", "sugar", "eggs", "chocolate chips")

# Initialize booleans for each ingredient to track them
flour_present = False
butter_present = False
sugar_present = False
eggs_present = False
chocolate_chips_present = False

# Prompt the user for ingredients until they enter "stop" and then break
while True:
    user_input = input("Please enter as many ingredients as you want. Once you are done, enter 'stop'. ")
    if user_input == "stop":
        break

    # Use multiple conditionals to check whether the user inputs any of the necessary ingredients
    if user_input == "flour":
        flour_present = True
    elif user_input == "butter":
        butter_present = True
    elif user_input == "sugar":
        sugar_present = True
    elif user_input == "eggs":
        eggs_present = True
    elif user_input == "chocolate chips":
        chocolate_chips_present = True
    else:
        print("This ingredient doesn't work for chocolate chip cookies!!!")

# Check if all required ingredients are present
if flour_present and butter_present and sugar_present and eggs_present and chocolate_chips_present:
    print("YAY! You can make chocolate chip cookies!")
else:
    print("You are missing some ingredients. Can't make chocolate chip cookies :(")

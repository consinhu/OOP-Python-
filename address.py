first_name = input("What is your first name?")
last_name = input("What is your last name?")
street_address = input("What is your street address?")
city = input("What is your city?")
state = input("What is your state?")
zip_code = input("What is your zipcode?")
print(f"Your mailing address should be structured as:\n{first_name.title()} {last_name.title()}\n{street_address.title()}\n{city.title()}, {state.upper()} {zip_code}")
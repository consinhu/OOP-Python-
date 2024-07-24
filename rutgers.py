# Could not import random module because it kept giving me import error
# Existing full names list
full_names = ["Alex Johnson", "Samantha Lee", "Juan Rodriguez", "Aaliyah Patel", "Daniel Kim", "Fatima Ali", "Adam Smith"]

# Empty list of email addresses
rutgers_emails = []

# Use for loop to iterate over each full name
for name in full_names:
    # Split full name into first and last name
    first_name, last_name = name.split()

    # Generate random 3-digit integers
    random_num = len(rutgers_emails) * 123 % 900 + 100

    # Create Rutgers email address
    emailaddress = f"{first_name[0].lower()}{last_name[0].lower()}{random_num}@rutgers.edu"

    # Append email address to rutgers emails list
    rutgers_emails.append(emailaddress)

print(rutgers_emails)
#Initialize variables for holding values that will be used for computing the average and incrementing
total = 0
entries = 0

#Initialize a variable that will accepts string inputs
#Make a while loop that breaks with user input when user input is stop
#Else if user input does not equal stop, total will increment by what integer the user inputs (convert user input variable to an int) and entries will increment by 1
while True:
    user_input = input("Please enter as many numbers as you'd like. When you are finished, enter 'stop'.")
    if user_input == 'stop':
        break
    else:
        total += int(user_input)
        entries += 1

#Once at least one entry is present, use a conditional for computing average of user's inputs by dividing total sum of user inputs and number of entries
#Print average of numbers entered by user
if entries > 0:
    avg = total/entries
    print(f"The average of the numbers you entered is: {avg}")

    


        
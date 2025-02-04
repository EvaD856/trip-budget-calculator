#Asks for information for total calculation

airfare = int(input("Please enter cost of airfare per person: $"))
print("")

food = int(input("Please enter daily food budget per person: $"))
print("")

days = int(input("Please enter the number of days the trip will be: "))
print("")

excursion = int(input("Please enter the excursion budget for the whole family: $"))
print("")

souvenir = int(input("Please enter the souvenir budget for the whole family: $"))
print("")

###################################################################################

#Calculates trip total

total = (airfare * 4) + (food * 4 * days) + excursion + souvenir

#####################################################################

# Checks if trip total is within budget
leftOver = 6000 - total

if total < 6000:
    print("#################################################################################")
    print("#                                                                               #")
    print("#  You are under budget. Total is $", total, ". You have $",leftOver,"leftover. #")
    print("#                                                                               #")
    print("#################################################################################")


elif total > 6000:
    print("You are over budget, you should reduce spending where you can.")

else:
    print("You are at exactly $6000!")

############################################################################################
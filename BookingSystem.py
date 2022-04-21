from datetime import date
import datetime
import random

def checkIntInuput(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        return True
    except ValueError:
        print("No.. input is not a number. It's a string")
        return False


def displayTicketInfo():
    print("=================================================================================")
    print("[Cost for one day:]")
    print("One Adult ---------------- $20.00")
    print("One Child ---------------- $12.00")
    print("One Senior --------------- $16.00")
    print("Family Ticket ------------ $60.00 (up to two adults or seniors, and three children)")
    print("Group Ticket ------------- $15.00 (at least six people. Price per person is $15)")
    print("--------------------------------------------------------------------------------")
    print("[Cost for two days:]")
    print("One Adult ---------------- $30.00")
    print("One Child ---------------- $18.00")
    print("One Senior --------------- $24.00")
    print("Family Ticket ------------ $90.00 (up to two adults or seniors, and three children)")
    print("Group Ticket ------------- $22.50 (at least six people. Price per person is $15)")
    print("--------------------------------------------------------------------------------")
    print("[Cost for Extra attraction:]")
    print("lion feeding    ---------- $2.50")
    print("Penguin feeding ---------- $2.00")
    print("evening barbecue --------- $5.00 (two-day tickets only)")
    print("=================================================================================")

def displayDaysAvaliable():
    print("=================================================================================")
    print("Dates avaliable:")
    today = date.today()
    for x in range(0,7):
        day = datetime.date.today() + datetime.timedelta(days=x)
        print(day)
    print("=================================================================================")

def displayDateSelection():
    print("=================================================================================")
    print("You are now at the booking system to select date")
    print("Type 0 to exit the booking system")
    
    today = date.today()
    for x in range(0,7):
        day = datetime.date.today() + datetime.timedelta(days=x)
        print("Type " + str(x+1) + " to select " + str(day))
    userIn = input("Please type here : ")
    while (checkIntInuput(input) == False):
        userIn = input("Invalid Input. Please re-type here : ")
    while int(userIn)<0 or int(userIn)>7:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    if (int(userIn) == 0):
        return 0
    return (datetime.date.today() + datetime.timedelta(days=int(userIn)-1))

def displayMenuAndGetInput():
    print("=================================================================================")
    print("You are now at the booking system to select ticket option")
    print("Type 0 to exit the booking system")
    print("Type 1 to book tickets for one day")
    print("Type 2 to book tickets for two days")
    print("Type 3 to purchase extra attraaction")
    userIn = input("Please type here : ")
    while int(userIn)<0 or int(userIn)>3:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def displaySubMenuDay():
    print("=================================================================================")
    print("Type 0 to exit the booking system")
    print("Type 1 for buying Adult ticket(s)")
    print("Type 2 for buying Child ticket(s)")
    print("Type 3 for buying Senior ticket(s)")
    print("Type 4 for buying Family ticket(s)")
    print("Type 5 for buying Group ticket(s)")
    userIn = input("Please type here : ")
    while int(userIn)<0 or int(userIn)>5:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def displaySubMenuExtra():
    print("=================================================================================")
    print("Type 0 to exit the booking system")
    print("Type 1 for buying lion feeding extra attraction")
    print("Type 2 for buying penguin feeding extra attraction")
    print("Type 3 for buying evening barbecue (two-day tickets only) extra attraction")
    userIn = input("Please type here : ")
    while int(userIn)<0 or int(userIn)>3:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def askTicketAmount():
    print("=================================================================================")
    print("How many tickets you want to buy?")
    userIn = input("Please type here : ")
    while int(userIn)<0:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def calTotalCost(usersTicketNo, ticketPrice):
    cost = 0
    for i in range(len(usersTicketNo)):
        for j in range(len(usersTicketNo[i])):
            for k in range(len(usersTicketNo[i][j])):
                cost += int(usersTicketNo[i][j][k]) * ticketPrice[j][k]
    return cost

def getBookingNumber():
    today = date.today()
    file = open("bookingNumber.txt", "r")
    existNumList = file.readlines()

    ranNumber = round(random.random()*1000)
    result = str(today.year) + str(f"{today.month:02d}") + str(f"{today.day:02d}") + str(f"{ranNumber:04d}") 
    for count in existNumList:
        if (result == int(count)):
            result = getBookingNumber()
    file.close()
    file = open("bookingNumber.txt", "a")
    file.writelines(result + "\n")
    file.close()

    return str(result)

def displayResult(usersTicketNo,ticketPrice):
    
    dictOfj = {0:"One Day Tickt:" , 1:"Two Days Ticket:" , 2:"Extra Attraction:"}
    dictOfk1 = {0:"Adult:" , 1:"Child:" , 2:"Senior:" , 3:"Family:" , 4:"Group:"}
    dictOfk2 = {0:"lion feeding:" , 1:"penguin feeding:" , 2:"evening barbecue:"}

    print("=================================================================================")
    print("The result of your booking infomation is shown below")
    print("Your booking number is " + str(getBookingNumber()))
    for i in range(len(usersTicketNo)):
        for j in range(len(usersTicketNo[i])):
            for k in range(len(usersTicketNo[i][j])):
                if usersTicketNo[i][j][k] !=0:
                    print(str(datetime.date.today() + datetime.timedelta(days=i)) , end=": ")
                    print(str(dictOfj[j]) , end=" ")
                    if(j!=2):
                        print(str(dictOfk1[k]), str(usersTicketNo[i][j][k]))
                    else:
                        print(str(dictOfk2[k]), str(usersTicketNo[i][j][k]))
    
    cost = calTotalCost(usersTicketNo, ticketPrice)
    print("Total Cost = $" + str(cost))
    print("=================================================================================")

def calBetterOption():
    return



# Main Function

displayDaysAvaliable()
displayTicketInfo()

usersTicketNo = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]]]
ticketPrice = [[20,12,16,60,15],[30,18,24,90,22.5],[2.5,2,5]]

while (True):

    ticketDate = displayDateSelection()
    if(ticketDate == 0):
        break
    dateIndex = (ticketDate - date.today()).days

    menuIn = int(displayMenuAndGetInput())
    
    #exit
    if (menuIn == 0):
        break

    #One Day or Two Days
    elif (menuIn == 1 or menuIn == 2):
        subMenuIn = displaySubMenuDay()
        if subMenuIn == 0:
            break
        amount = askTicketAmount()

    #Extra
    else:
        subMenuIn = displaySubMenuExtra()
        if subMenuIn == 0:
            break
        amount = askTicketAmount()
    
    usersTicketNo[dateIndex][menuIn-1][subMenuIn-1] = amount


displayResult(usersTicketNo,ticketPrice)
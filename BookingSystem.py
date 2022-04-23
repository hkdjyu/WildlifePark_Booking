from datetime import date
import datetime
import random
import copy

def checkIntInuput(input):
    # Exception handling
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        print("Input is not a number. It's a string")
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
        # day = date of today + changeOfDay i.e. today, tomorrow, day after tomorrow ...
        day = datetime.date.today() + datetime.timedelta(days=x)
        print(day)
    print("=================================================================================")

def askDateSelection():
    print("=================================================================================")
    print("You are now at the booking system to select date")
    print("Type 0 to exit the booking system")
    
    today = date.today()
    for x in range(0,7):
        day = datetime.date.today() + datetime.timedelta(days=x)
        print("Type " + str(x+1) + " to select " + str(day))
    userIn = input("Please type here : ")
    while (checkIntInuput(userIn) == False):
        userIn = input("Invalid Input. Please re-type here : ")
    while int(userIn)<0 or int(userIn)>7:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")

    # user exit the system
    if (int(userIn) == 0):
        return 0
    # return (date of today + changeOfDay) i.e. today or tomorrow or...
    return (datetime.date.today() + datetime.timedelta(days=int(userIn)-1))

def askMenuAndGetInput():
    print("=================================================================================")
    print("You are now at the booking system to select ticket option")
    print("Type 0 to exit the booking system")
    print("Type 1 to book tickets for one day")
    print("Type 2 to book tickets for two days")
    userIn = input("Please type here : ")
    while (checkIntInuput(userIn) == False):
        userIn = input("Invalid Input. Please re-type here : ")
    while int(userIn)<0 or int(userIn)>2:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def askSubMenuType():
    print("=================================================================================")
    print("Which type of ticket you want to buy?")
    print("Type 0 to exit the booking system")
    print("Type 1 for buying Adult ticket(s)")
    print("Type 2 for buying Child ticket(s)")
    print("Type 3 for buying Senior ticket(s)")
    print("Type 4 for buying Family ticket(s)")
    print("Type 5 for buying Group ticket(s)")
    userIn = input("Please type here : ")
    while (checkIntInuput(userIn) == False):
        userIn = input("Invalid Input. Please re-type here : ")
    while int(userIn)<0 or int(userIn)>5:
        userIn = input("Invalid Input. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def askSubMenuExtra(dayOption):
    # two-day extra attraction
    if dayOption == 2:
        print("=================================================================================")
        print("Do you want to buy some extra attraction?")
        print("Type 0 to continue the booking")
        print("Type 1 for buying lion feeding extra attraction")
        print("Type 2 for buying penguin feeding extra attraction")
        print("Type 3 for buying evening barbecue extra attraction")
        userIn = input("Please type here : ")
        while (checkIntInuput(userIn) == False):
            userIn = input("Invalid Input. Please re-type here : ")
        while int(userIn)<0 or int(userIn)>3:
            userIn = input("Invalid Input. Please re-type here : ")
        print("=================================================================================")
        return int(userIn)
    # one-day extra attraction
    if dayOption == 1:
        print("=================================================================================")
        print("Do you want to buy some extra attraction?")
        print("Type 0 to continue the booking")
        print("Type 1 for buying lion feeding extra attraction")
        print("Type 2 for buying penguin feeding extra attraction")
        userIn = input("Please type here : ")
        while (checkIntInuput(userIn) == False):
            userIn = input("Invalid Input. Please re-type here : ")
        while int(userIn)<0 or int(userIn)>2:
            userIn = input("Invalid Input. Please re-type here : ")
        print("=================================================================================")
        return int(userIn)

def askTicketAmount(min, maxExtra):
    print("=================================================================================")

    if maxExtra == 0:
        print("You cannot buy the option or you have bought the maxmimum amount of the option.")
        print("Returning to the booking system...")
        print("=================================================================================")
        return 0
    
    print("How many tickets you want to buy?")
    userIn = input("Please type here : ")
    while (checkIntInuput(userIn) == False):
        userIn = input("Invalid Input. Please re-type here : ")
    while int(userIn)<min:
        print("You need to but at least", min ,"ticket(s). Please re-type here : ", end="")
        userIn = input()

    if maxExtra > 0:
        while int(userIn) > maxExtra:
            userIn = input("Your order exceeds the maximum. Please re-type here : ")
    print("=================================================================================")
    return int(userIn)

def calTotalCost(usersTicketNo, ticketPrice):
    cost = 0
    for i in range(len(usersTicketNo)):
        for j in range(len(usersTicketNo[i])):
            for k in range(len(usersTicketNo[i][j])):
                # cost = ticket amount * its cost
                cost += int(usersTicketNo[i][j][k]) * ticketPrice[j][k]
    return cost

def getBookingNumber():
    today = date.today()
    file = open("bookingNumber.txt", "r")

    # read file line by line and store it into a list
    existNumList = file.readlines()

    # obtain a random number in 4 digit
    ranNumber = round(random.random()*1000)

    # booking number = 12 digit in YYYYMMDDXXXX format
    result = str(today.year) + str(f"{today.month:02d}") + str(f"{today.day:02d}") + str(f"{ranNumber:04d}") 
    
    # check any repetition
    for existNumber in existNumList:
        if (result == int(existNumber)):
            result = getBookingNumber()
    file.close()

    # write file using append mode (will not replace existing number)
    file = open("bookingNumber.txt", "a")
    file.writelines(result + "\n")
    file.close()

    return str(result)

def displayResult(usersTicketNo,ticketPrice,mode):
    
    if mode == 1:

        #create 3 dictionaries for showing different infomation about tickets
        dictOfj = {0:"One Day Tickt:" , 1:"Two Days Ticket:" , 2:"Extra Attraction:"}
        dictOfk1 = {0:"Adult:" , 1:"Child:" , 2:"Senior:" , 3:"Family:" , 4:"Group:"}
        dictOfk2 = {0:"lion feeding:" , 1:"penguin feeding:" , 2:"evening barbecue:"}

        print("=================================================================================")
        print("The result of your booking infomation is shown below")
        bookingNumber = str(getBookingNumber())
        print("Your booking number is " + bookingNumber)

        for i in range(len(usersTicketNo)):
            for j in range(len(usersTicketNo[i])):
                for k in range(len(usersTicketNo[i][j])):
                    if usersTicketNo[i][j][k] !=0:
                        #print date
                        print(str(datetime.date.today() + datetime.timedelta(days=i)) , end=": ")
                        #print one-day or two-day or extra attraction
                        print(str(dictOfj[j]) , end=" ")
                        # not extra attraction
                        if(j!=2):
                            print(str(dictOfk1[k]), str(usersTicketNo[i][j][k]))
                        # is extra attraction
                        else:
                            print(str(dictOfk2[k]), str(usersTicketNo[i][j][k]))
        
        #calculate total cost
        cost = calTotalCost(usersTicketNo, ticketPrice)
        print("Total Cost = $" + str(cost))
        print("=================================================================================")
        
        # calculate a better choice and display info
        newTicketno = calBetterOption(usersTicketNo)
        if (usersTicketNo != newTicketno):
            print("=================================================================================")
            print("Your booking can be optimized and the result is shown below")
            print("Your booking number is " + bookingNumber)
            for i in range(len(newTicketno)):
                for j in range(len(newTicketno[i])):
                    for k in range(len(newTicketno[i][j])):
                        if newTicketno[i][j][k] !=0:
                            print(str(datetime.date.today() + datetime.timedelta(days=i)) , end=": ")
                            print(str(dictOfj[j]) , end=" ")
                            if(j!=2):
                                print(str(dictOfk1[k]), str(newTicketno[i][j][k]))
                            else:
                                print(str(dictOfk2[k]), str(newTicketno[i][j][k]))
            cost = calTotalCost(newTicketno, ticketPrice)
            print("Total Cost = $" + str(cost))
            print("=================================================================================")
            print("=================================================================================")
            print("You have finished the booking.")
            print("The booking system is closing now...")
            print("See you! Bye Bye!.")
            print("=================================================================================")
    
    # if the user does not buy ticket
    else:
        print("=================================================================================")
        print("You have not made any booking.")
        print("The booking system is closing now...")
        print("See you! Bye Bye!.")
        print("=================================================================================")

def calBetterOption(usersTicketNo):
    # The best option is to buy family tickets as much as possible
    # family > group > others
    list = copy.deepcopy(usersTicketNo) # list is a new list object instead of referencing usersTicketNo
    for i in range(len(usersTicketNo)):
        for j in range(0,2): #Consider one-day and two day tickets only
            # handle family
            if (list[i][j][1]//3 > 0): # child // 3, i.e. atleast 1 family
                list[i][j][3] += (list[i][j][1]//3) # family += child//3

                # initialize count = number of adult or senior ticket to be removed i.e. family ticket *2
                count = ((list[i][j][1]//3) * 2)
                while (count > 0):
                    # adult > 0
                    if (list[i][j][0] > 0):
                        list[i][j][0] -= 1
                    
                    # senior >0
                    elif(list[i][j][2] > 0):
                        list[i][j][2] -= 1

                    # update count
                    count -= 1
                
                # update child tickets amount
                list[i][j][1] = list[i][j][1]%3 #child = child mod 3

            # handle group tickets
            if (list[i][j][0] + list[i][j][2]) >= 6: # adult + senior >= 6
                list[i][j][4] += (((list[i][j][0] + list[i][j][2]) // 6) * 6) # group += ((adult + senior)//6) * 6
                
                 # initialize count = number of adult or senior ticket to be removed i.e. number of new group tickets
                count = (((list[i][j][0] + list[i][j][2]) // 6) * 6)
                while (count > 0):
                    if (list[i][j][0] > 0):
                        list[i][j][0] -= 1
                    elif(list[i][j][2] > 0):
                        list[i][j][2] -= 1
                    count -= 1

            # handle exception case (remaining: 1 child and 5 seniors)
            if (list[i][j][1]>=1 and list[i][j][2]>=5):
                list[i][j][4] += 6
                list[i][j][1] -= 1
                list[i][j][2] -= 5
    return list

# Main Function
def main():
    displayDaysAvaliable()
    displayTicketInfo()

    #initialize the amount of tickets bought by user
    #userTicketNo[date][day1orday2orextra][adultorchild... or lionorpenguin...]
    usersTicketNo = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]]]

    #initialize the ticketPrice accodring to the option
    ticketPrice = [[20,12,16,60,15],[30,18,24,90,22.5],[2.5,2,5]]

    # System while loop
    while (True):
        ticketDate = askDateSelection()
        if(ticketDate == 0):
            break

        # if today, dateIndex = 0 ; if tomorrow, dateIndex = 1
        dateIndex = (ticketDate - date.today()).days

        menuDay = int(askMenuAndGetInput())
        
        #exit system
        if (menuDay == 0):
            break

        #One Day(1) or Two Days(2)
        else:
            subMenuType = askSubMenuType()

            #exit system
            if subMenuType == 0:
                break
            
            # initialize min and max for validating the number of tickets
            min = 0
            max = -1 # unlimited

            # set group ticket min
            if subMenuType == 5:
                min = 6
            
            # set children ticket max
            if subMenuType == 2:
                max = (usersTicketNo[dateIndex][menuDay-1][0]+usersTicketNo[dateIndex][menuDay-1][2]) * 2

            # ask ticket amount
            amount = askTicketAmount(min,max)
            usersTicketNo[dateIndex][menuDay-1][subMenuType-1] += amount

            #handle extra attraction
            if amount>0:
                min = 0
                max = -1
                #one-day shows (1)(2) extra att. only
                subMenuExtra = askSubMenuExtra(menuDay)
                # maxExtra refers to the maximum extra attraction can the user buy
                # amount refers to the amount of tickets just bought by the user
                maxExtraList = [amount,amount,amount]

                # user buy extra attraction
                while subMenuExtra != 0:
                    # max refers to the maxExtraList
                    amount = askTicketAmount(min, maxExtraList[subMenuExtra-1])
                    maxExtraList[subMenuExtra-1] -= amount
                    #update the total amount of tickets bought by user
                    usersTicketNo[dateIndex][2][subMenuExtra-1] += amount
                    subMenuExtra = askSubMenuExtra(menuDay)

    #if user directly terminate the system
    if usersTicketNo == [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]],
                        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0]]]:
        displayResult(usersTicketNo,ticketPrice,0)

    #if user bought some tickets
    else:
        displayResult(usersTicketNo,ticketPrice,1)

#Program starts here
if __name__ == "__main__":
    main()

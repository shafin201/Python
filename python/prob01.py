#Available room for student
available_room = {501, 502, 503, 504}
#Available seat for student
available_seats = ["501A","501B","501C","501D","502A","502B","502C","502D","503A","503B","504A","504B","504C","504D"]
map = dict()
# This function for see available seat and map
def chooseSeat(available_seats,map) :
    print("Which seat you want to take")
    print("Available seats are")
    for i in available_seats:
        print(i);
# input room number
    userSelection = input("Enter the room number : ")
# input information
    if userSelection in available_seats:
        available_seats.remove(userSelection)
        userID = input("Enter your ID NO : ")
        if userID in map:
            print("You already have a room booked")
            return
        map[userID] = userSelection
        print("Your seat has been booked! ")
        print("ID No : ", userID)
        print("Room No : ",userSelection)
    else :
        print("Sorry. The room is not available")
def changeSeat( available_seats )  :
    if len(available_seats)==0 :
        print("You cannot change your seat. ")
    else:
        chooseSeat()
def cancelSeat(map) :
    userID = input("Enter your ID No : ")
    if userID in map :
        del map[userID]
def emergency(map):
    userID = input("Enter the student ID you want to search : ")
    if userID in map :
        print("The seat of the student is ",map[userID])
#print All options
while 0<1 :
    print("Select a option")
    print("1.Book Seat")
    print("2.Change Seat")
    print("3. Cancel Seat")
    print(("4.Emergency "))
    print("-1 TO EXIT .")
    userInput = int(input("Enter the option no : "))
    if userInput == -1 :
        break
    elif userInput == 1:
        chooseSeat(available_seats, map)
    elif userInput == 2:
        changeSeat(available_seats)
    elif userInput == 3:
        cancelSeat(map)
    elif userInput == 4:
        emergency(map)
import names
import os
import random
class Hotel:
    
    definition = "This is a hotel"

    def __init__(self, name):
        self.quantity = 0
        self.name = name
        self.Rooms = []
        self.floors = 0
        self.roomsPerFloor = 0

    #def (self)

    def showRooms(self):
        for room in self.Rooms:
            room.info()
            
    def showCleanRooms(self):
            for room in self.Rooms:
                if len(room.guests) == 0 and room.cond == "Clean":
                     room.info()

    def checkIn(self, Person):
        for room in self.Rooms:
            if Person.full_nam in room.guests and room.checkedIn == False:
                room.checkedIn = True
                print(Person.full_nam + " checked in into room: " + str(room.rn))
                break
            else:
                print("No rooms available")

    def reservation(self, Person):
        for room in self.Rooms:
            if len(room.guests) == 0 and room.cond == "Clean":
                room.guests.append(Person)
                print("Reservation made for: " + Person.full_name + ", allocated room: " + str(room.rn))
                break
                
    def reservationRoom(self, Person, room):
            if len(room.guests) == 0 and room.cond == "Clean":
                room.guests.append(Person)
                print("Reservation made for: " + Person.full_name + ", allocated room: " + str(room.rn))
                

class Room(Hotel):
    definition = "This is a room"
    room_categories = ["Standard Room","Standard Queen-Economy","Standard Queen","Standard Twin","Superior Twin","Superior Extra"]
    amountOfRooms = 0

    def __init__(self, roomnumber):
        self.checkedIn = False
        self.guests = []
        self.rt = random.choice(Room.room_categories)
        self.rn = str(roomnumber)
        self.cond = "Clean"
    

    def info(self):
        print("Nr: " + str(self.rn) + ", Type: " + self.rt + ", Cond: " + self.cond) 



class Person():

    def __init__(self):
        self.firstName = names.get_first_name()
        self.lastName = names.get_last_name()
        self.full_name = self.firstName + " " + self.lastName
        self.Rooms = []
    



def confHotel(hotel):
    #What this function does is that it generates a hotel with randomly allocated rooms
    roomsFloor = random.randint(2,10)
    floors = random.randint(2,10)
    hotel.quantity = roomsFloor * floors
    hotel.floors = floors
    hotel.roomsPerFloor = roomsFloor
    numberScaler = 2
    if len(str(hotel.quantity)) > 3:
        numberscale = len(str(hotel.quantity))
        
    
    for i in range(1,floors):
        for j in range(1, roomsFloor):
            hotel.Rooms.append(Room(i*10**(numberScaler)+j))
        
    print("floors: " + str(floors) + " , roomsFloor: " + str(roomsFloor))

h = Hotel('Scandic')
p = Person()

confHotel(h)

#h.showRooms()

h.reservation(p)





loggedin = True

while(loggedin):
    print ('''
    1. Reservation
    2. Check-in
    3. Check-out
    4. Log out


    ''')
    user_input = input("What would you like to do? (1-4): ")

    if user_input == "1":
        print("RESERVATION")
        print("These are the available rooms: ")
        h.showCleanRooms()
        roomReq = input("Which room would you like to reserve?: ")
        #personName = input("What's your name?: ")
        for room in h.Rooms:
            if room.rn == str(roomReq):
                h.reservationRoom(Person(),room)
                break                    
   
    elif user_input == "2":
        print("CHECK-IN")
        personName = input("Please enter your name: ")
        for room in h.Rooms:
            if personName in room.guests:
                println("You " + personName + " have been assigned to room " + str(room.rn))
                break
            else:
                print("Sorry we could not find that person, please try again!")
    elif user_input == "3":
        print("CHECK-OUT")
    elif user_input == "4":
        print("Bye bye!")
        loggedin = False
    elif user_input == "-1":
        os.system('clear')
        print("ADMIN")
            
    else:
        print("enter a number")























    
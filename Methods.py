moviesList = {}

def AddMovie(nameOfMovie: str, prise: int, allSeats: int):
    moviesList.setdefault(nameOfMovie)

    moviesList[nameOfMovie] = [prise, allSeats]

    return moviesList

def ToString():
    for movie, (price, seats) in moviesList.items():
        print(f"Movie: {movie}, price: {price}, seats: {seats}")

bookedSeatsList = {}

def BookTickets(chosenMovie: str):
    if chosenMovie not in moviesList.keys():
        print("The movie was not found.")
    else:
        print(f"This movie has {moviesList[chosenMovie][1]} free seats.")

        print("Print the number of seats you want to book:")
        bookenSeats = int(input())

        if moviesList[chosenMovie][1] < bookenSeats:
            print("Not enought free seats.")
        else:
            moviesList[chosenMovie][1] -= bookenSeats
            bookedSeatsList.update({chosenMovie : bookenSeats})
            finalcost = bookenSeats * moviesList[chosenMovie][0]
            print(f"You booked {bookenSeats} seats, it cost {finalcost}$.")

def CancelTickets(chosenMovie: str):
    if chosenMovie not in bookedSeatsList.keys():
        print("The movie was not found.")
    else:
        bookedSeats = bookedSeatsList.get(chosenMovie)
        print(f"You booked {bookedSeats} seats in this movie.")
        print("How many of seats do you want to cancel?")
        seatsForCansel = int(input())

        if seatsForCansel > bookedSeats:
            print("You can not cancel more than you have booked!")
        else:
            bookedSeats -= seatsForCansel
            moviesList[chosenMovie][1] += seatsForCansel
            costBack = seatsForCansel * moviesList[chosenMovie][0]
            print(f"You cancelled {seatsForCansel} seats and got {costBack}$ back.")
moviesList = {}
moviesList["Spider-Man"] = []
moviesList["Spider-Man"].append(50)
moviesList["Spider-Man"].append(10)

moviesList["Avengers"] = []
moviesList["Avengers"].append(45)
moviesList["Avengers"].append(15)


print("Welcome to our cinema!")
print("There are the options you can choose: \n1. Add a movie " \
"\n2. View movies \n3. Book tickets \n4. Cancel tickets \n5. Exit programm")

bookTickets = {}
chosenOption = 0

while chosenOption != 5:
    print("What service would you prefer?")
    chosenOption = input() 
    if chosenOption == "1":
        print("Enter movie name:")
        inpMovie = input()
        
        inpSeats = 55
        while inpSeats > 50:
            print("Enter number of free seats:")
            inpSeats = int(input())
            if inpSeats > 50:
                print("You can't have more than 50 free seats")
            else:
                break

        print("Enter movie price:")
        inpPrize = int(input())

        moviesList.update({inpMovie : [inpSeats, inpPrize]})

        print("Your movies list was updated")
    
    elif chosenOption == "2":
        print("Here is your movies list:")
        print(moviesList)


    elif chosenOption == "3":
            print("Choose a movie:")
            chosenMovie = input()
            if chosenMovie in moviesList.keys():

                seatsOfMovie = moviesList.get(chosenMovie)[0]

                print(f"The movie {chosenMovie} has {seatsOfMovie} free seats")
                print("Print the number of seats you want to book:")
                amountOfSeats = int(input())
                if amountOfSeats <= seatsOfMovie:
                    updatedSeats = seatsOfMovie - amountOfSeats
                    print(f"The movie {chosenMovie} has now {updatedSeats} free seats")
                    bookTickets[chosenMovie] = [amountOfSeats]

                    print(f"You paid {moviesList.get(chosenMovie)[1] * amountOfSeats} euros to book these seats/this seat")
            else:
                print("The film wasn't found, try again after looking at the movies list")

    
    elif chosenOption == "4":
        print("Select a movie which you want to cancel tickets:")
        movieTitel = input()

        if movieTitel in bookTickets.keys():
            
            stop = False
            while stop != True:
                print(f"You booked {bookTickets.get(movieTitel)[0]} tickets. Do you want to return them?")
                print("1. Yes, 2. No")
                returnOrNot = int(input())
                if returnOrNot == 1:
                    moviesList.get(movieTitel)[0] + bookTickets.get(movieTitel)[0]
                    print(f"Aright, the movie {movieTitel} has {moviesList.get(movieTitel)[0]} free seats now")
                    
                    bookTickets.pop(movieTitel)
                    stop = True
                else:
                    stop = True

        else:
            print(f"The movie {movieTitel} was not found.\
                  \nThere may have been an input error or the tickets were not booked")
            
    if chosenOption == "5":
        print("Thank you for visiting our cinema, see you again!")
        break
        
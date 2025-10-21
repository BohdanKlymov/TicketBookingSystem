fetch("http://localhost:5000/get-all")
.then((response) => response.json())
  .then((json) => {
    console.log(json);

    const link = "C:/AllMyProgramming/WebCinema/moviePictures/"; 
    const divList = document.getElementById("list");
    const bookButton = document.getElementById("book");

    let selectedMovie = null;
    let numberOfTickets = null;

    json.forEach((movie) => {
      const movieBlock = document.createElement("div");
      movieBlock.classList.add("movie-block");
      movieBlock.innerHTML = `
      <img src="${link + movie.movie_picture}" height="75%">
      <h3 class="inf-to-movie">${movie.title}</h3>
      `;
      const infInMovieBlock = document.createElement("div");
      infInMovieBlock.classList.add("inf-in-movie-block");
      movieBlock.appendChild(infInMovieBlock);
      infInMovieBlock.innerHTML = `
        <p class="inf-to-movie">Jear: ${movie.movie_yearOfRelease}</p>
        <p class="inf-to-movie">Cost: ${movie.price}$</p>
      `;
      divList.appendChild(movieBlock);

      movieBlock.addEventListener("click", () => {
        document.getElementById("movie-output").innerHTML = movie.movie_description;
        document.getElementById("moviename-output").innerHTML = movie.title;

        selectedMovie = movie;
      });

      const input = document.getElementById("inputOfTickets");
      numberOfTickets = input;
    });

    bookButton.addEventListener("click", () => {
      const amountInput = document.getElementById("inputOfTickets").value;
      const amount = parseInt(amountInput, 10);

      if (selectedMovie) {
        if (isNaN(amount) || amount <= 0) {
          alert("Please enter a valid number of tickets!");
        } else {
          alert(`You booked ${amount} ticket(s).`);
          alert(`You paid ${selectedMovie.price * amount}$`);
        } 
      } else {
        alert("Please select a movie first!");
      }
    });
  })

  
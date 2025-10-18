fetch("http://localhost:5000/get-all")
  .then((response) => response.json())
  .then((json) => {
    console.log(json);

    const link = "C:\\AllMyProgramming\\WebCinema\\moviePictures"

    const divList = document.getElementById("list");

    json.forEach((movie) => {
      const movieBlock = document.createElement("div");
      movieBlock.classList.add("movie-block");
      movieBlock.innerHTML = `
        <img src=${link + movie.movie_picture} height="75%">
        <h3>${movie.title}</h3>
        <p>${movie.movie_yearOfRelease}</p>
        <p>${movie.price}$</p>
      `;
      divList.appendChild(movieBlock);

      movieBlock.addEventListener("click", () => {
        document.getElementById("movie-output").innerHTML = movie.movie_description;
      });
      
      movieBlock.addEventListener("click", () => {
        document.getElementById("moviename-output").innerHTML = movie.title;
      });
    });
  })
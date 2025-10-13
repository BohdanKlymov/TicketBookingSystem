fetch("http://localhost:5000/get-all")
  .then((response) => response.json())
  .then((json) => {
    console.log(json);

    const divList = document.getElementById("list");
    divList.innerHTML = "";

    json.forEach((movie) => {
      const movieBlock = document.createElement("div");
      movieBlock.classList.add("movie-block");

      movieBlock.innerHTML = `
        <button id="movie">
          <h3>${movie.title}</h3>
          <p>${movie.movie_description}</p>
          <p>${movie.price}$</p>
        </button>
      `;

      divList.appendChild(movieBlock);

      document.getElementById("movie").addEventListener("click", clickOnMovie);

      
      function clickOnMovie() {
        document.getElementById("maintance-con").innerHTML = movie.title;
      }


    });
  })
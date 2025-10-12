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
        <h3>${movie.title}</h3>
        <p>${movie.movie_description}</p>
      `;

      divList.appendChild(movieBlock);
    });
  })
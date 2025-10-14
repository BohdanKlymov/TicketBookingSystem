fetch("http://localhost:5000/get-all")
  .then((response) => response.json())
  .then((json) => {
    console.log(json);

    const divList = document.getElementById("list");
    divList.innerHTML = "";

    json.forEach((movie) => {
      const movieBlock = document.createElement("div");
      movieBlock.classList.add("movie-block");

      const btn = document.createElement("button");
      btn.setAttribute("id", "movies-buttons");
      btn.classList.add("movie-btn");
      btn.innerHTML = `
        <img>${movie.movie_picture}</img>
        <h3>${movie.title}</h3>
        <p>${movie.movie_jearOfRelease}</p>
        <p>${movie.price}$</p>
      `;

      btn.addEventListener("click", () => {
        document.getElementById("movie-output").innerHTML = movie.movie_description;
      });

      movieBlock.appendChild(btn);
      divList.appendChild(movieBlock);
    });
  })
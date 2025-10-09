fetch("http://localhost:5000/get-all")
  .then((response) => response.json())
  .then((json) => {
    console.log(json);


  const child = document.createElement("p");
  child.innerHTML = JSON.stringify(json, null, 2);

  const divList = document.getElementById("list");
  divList.appendChild(child)

  const picturesLink = "C:\AllMyProgramming\WebCinema\moviePictures";

  var img = document.createElement("img");
  img.src = picturesLink + "\download (2).jpg"
  divList.appendChild(img)
})
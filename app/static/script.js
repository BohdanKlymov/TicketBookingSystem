fetch("http://localhost:5000/get-all")
  .then((response) => response.json())
  .then((json) => console.log(json));
function validate() {
  var username = document.getElementById("floatingInput").value;
  var password = document.getElementById("floatingPassword").value;
  if (
    (username == "mitrc" && password == "admin") ||
    (username == "liet" && password == "alwar") ||
    (username == "Lords" && password == "university")
  ) {
    window.open("Letter.html", "_self");
  } else {
    alert("Incorrect Credentials");
  }
}

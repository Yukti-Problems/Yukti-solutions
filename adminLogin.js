function validate() {
    var username = document.getElementById("floatingInput").value;
    var password = document.getElementById("floatingPassword").value;
    if (
      (username == "admin1" && password == "admin1") ||
      (username == "admin2" && password == "admin2") ||
      (username == "admin3" && password == "admin3")
    ) {
      window.open("adminDashboard.html", "_self");
    } else {
      alert("Incorrect Credentials");
    }
  }
  
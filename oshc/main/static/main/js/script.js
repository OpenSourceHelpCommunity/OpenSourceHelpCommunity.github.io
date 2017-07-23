$(document).ready(function() {

  $("#toTop").click(function() {
    $("html, body").animate({
      scrollTop: 0
    }, 1000);
  });
  //  code for PASSWORD STRENGTH METER
  $(".strength-wrapper").css("visibility", "hidden"); //hide the strength meter initially
  console.log("checker2");
  $("#id_password1").bind("keyup", function() {
    if ($(this).val().length === 0) {
      $(".strength-wrapper").css("visibility", "hidden");//hide the strength meter when the password field is empty
      $("#passwordStrengthString").html("");

      return;
    } else {
      $(".strength-wrapper").css("visibility", "visible");
    }
    var check = ["[A-Z]", "[a-z]", "[0-9]", "[$@$!%*#?&]"];//takes all uppercase & lowercase alphabets,digits,special characters

    var checkCounter = 0;
    for (var i = 0, len = check.length; i < len; i++) {
      if (new RegExp(check[i]).test($(this).val())) {      //checks the password 
        checkCounter++;
      }
    }
    if (checkCounter > 2 && $(this).val().length > 8) {
      checkCounter++;
    }
    var passwordStrength = "";
    // strength meter display depending upon the value of checkCounter
    switch (checkCounter) {
      case 0:
      case 1:
        passwordStrength = "Weak";
        $(".weak").css("background-color", "#E53935");
        $(".good").css("background-color", "#EEEEEE");
        $(".strong").css("background-color", "#EEEEEE");
        $(".verystrong").css("background-color", "#EEEEEE");
        $("#passwordStrengthString").css("color", "#E53935");
        break;
      case 2:
      case 3:
        passwordStrength = "Good";
        $(".weak").css("background-color", "#FFEB3B");
        $(".good").css("background-color", "#FFEB3B");
        $(".strong").css("background-color", "#EEEEEE");
        $(".verystrong").css("background-color", "#EEEEEE");
        $("#passwordStrengthString").css("color", "#FFEB3B");
        break;
      case 4:
        passwordStrength = "Strong";
        $(".weak").css("background-color", "#64DD17");
        $(".good").css("background-color", "#64DD17");
        $(".strong").css("background-color", "#64DD17");
        $(".verystrong").css("background-color", "#EEEEEE");
        $("#passwordStrengthString").css("color", "#64DD17");
        break;
      case 5:
        passwordStrength = "Very Strong";
        $(".weak").css("background-color", "#2E7D32");
        $(".good").css("background-color", "#2E7D32");
        $(".strong").css("background-color", "#2E7D32");
        $(".verystrong").css("background-color", "#2E7D32");
        $("#passwordStrengthString").css("color", "#2E7D32");
        break;
    }
    $("#passwordStrengthString").html(passwordStrength);// returns the strength string to the html
  });
});

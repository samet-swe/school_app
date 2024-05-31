document.addEventListener("DOMContentLoaded", function() {
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const context = JSON.parse(document.getElementById("context").textContent);

    document.getElementById("submitButton").addEventListener("click", function() {
        const userInput = username.value.toLowerCase();
        const pwdInput = password.value;

        var userExists = 0;
        var role = "";
        var userId = 0;

        alert("js loaded ");
        try {
            if (pwdInput.localeCompare(context[0][userInput][0]) == 0) {
                alert("username/pwd match");
                role = context[0][userInput][1];
                userId = context[0][userInput][2];
                alert(userId);
                userExists = 1;
            }
            else {
                alert("Password does not match.");
            }
        }
        catch (err) {
            alert("Username does not exist.  " + err);
        }

        if (userExists == 1) {
            alert("match found, check role");
            switch (role) {
                case "Te":
                    alert("/teacher/" + userId);
                    location.href = "/teacher/" + userId;
                    break;
                case "St", "Pa":
                    location.href = "/student/" + userId;
                    break;
                case "Of":
                    location.href = "/home";
                    break;
                default:

            }
            /* if (role.localeCompare("Te") == 0) {
                location.href = "/teacher/" + userId
            }
            else if (role.localeCompare("St") == 0) {
                alert("Not Teacher");
            } */
        }
        else {
            alert("Username or password does not exist.");
        }
    });
});
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

        try {
            if (pwdInput.localeCompare(context[0][userInput][0]) == 0) {
                role = context[0][userInput][1];
                userId = context[0][userInput][2];
                userExists = 1;
            }
            /*else {
                alert("Password does not match.");
            }*/
        }
        catch (err) {
            /*alert("Username does not exist.  " + err);*/
        }

        if (userExists == 1) {
            switch (role) {
                case "Te":
                    location.href = "/teacher/" + userId;
                    break;
                case "Pa":
                    location.href = "/student/" + userId;
                    break;                
                case "St":
                    location.href = "/student/" + userId;
                    break;
                case "Of":
                    location.href = "/office/" + userId;
                    break;
                default:

            }
        }
        else {
            alert("Username or password does not exist.");
        }
    });
});
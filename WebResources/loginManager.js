
function checkLogin(){
    console.log("Checking login");
    console.log(localStorage.getItem('currentUserID'));
    if (localStorage.getItem('currentUserID') != "" && localStorage.getItem('currentUserID') != null) {
        console.log("User is logged in");
        updateNavBarItem(true);
    } else {
        console.log("User is NOT logged in");
        updateNavBarItem(false);
    }
}

function updateNavBarItem(logged){
    if(logged == true){
        document.getElementById("userButton").innerHTML = `
        <a class="nav-link active" aria-current="page" href="profile">
            <img src="/WebResources/user.png" alt="Admin" class="rounded-circle" width="40">
        </a>
        `;
    } else {
        document.getElementById("userButton").innerHTML = `
        <a class="nav-link active" aria-current="page" href="loginregister">Log in to Patient Account</a>
        `;
    }
    
}
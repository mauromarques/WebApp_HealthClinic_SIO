serviceJsonData = [{}];
doctorJsonData = [{}];

function getServices(){
    console.log("GET SERVICES")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            serviceJsonData = jsonData;
            getDoctors();
        }
    };
    xhttp.open("GET", "getServices", true);
    xhttp.send();
}

function getUserInfo(){
    console.log("GET User Info")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            document.getElementById("userTitle").innerHTML = jsonData[0]["name"];
            document.getElementById("userName").innerHTML = jsonData[0]["name"];
            document.getElementById("userEmail").innerHTML = jsonData[0]["email"];
        }
    };
    xhttp.open("GET", "getUserInfo/?userID="+localStorage.getItem('currentUserID'), true);
    xhttp.send();
}

function getBookingsByUser(){
    console.log("GET Bookings")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        serviceData = []
        doctorData = []
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            for(var j = 0; j< jsonData.length; j++){
                //Service info
                for(var i = 0; i< serviceJsonData.length; i++){
                    if(serviceJsonData[i]["serviceID"] == jsonData[j]["serviceID"]){
                        serviceData.push(serviceJsonData[i])
                    }
                }
                //Doctor info
                for(var i = 0; i< doctorJsonData.length; i++){
                    if(doctorJsonData[i]["doctorID"] == jsonData[j]["doctorID"]){
                        doctorData.push(doctorJsonData[i])
                    }
                }
            }

            list1 = "";
            for (var i = 0; i< jsonData.length; i++){
                sampleData = jsonData[i];
                list1 = list1 + `
                    <li class="list-group-item text-secondary" style="padding: 1rem;"">
                        <b>`+sampleData["date"]+`:    `+serviceData[i]["name"]+`</b>
                        <br>   - Doctor: `+doctorData[i]["name"]+`, Ratings: `+doctorData[i]["ratings"]+`
                        <br>   - Service: `+serviceData[i]["name"]+`, Price: `+serviceData[i]["price"]+`
                    </li>
                `;
            }
            document.getElementById("appointmentsListUser").innerHTML = list1;
        }
    };
    xhttp.open("GET", "getBookingsByUser/?userID="+localStorage.getItem('currentUserID'), true);
    xhttp.send();
  }

  function loadProfile(){
    getServices()
  }

  function getDoctors(){
    console.log("GET DOCTORS")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            doctorJsonData = jsonData;
            getBookingsByUser();
        }
    };
    xhttp.open("GET", "getDoctors", true);
    xhttp.send();
  }

  function logout(){
    localStorage.setItem('currentUserID', "");
    window.location.href = "/loginregister";
  }

  function downloadButton(){
    let code = prompt("Please enter your test result code", "");
    if (code != null && code != "") {
        console.log(code)
        getTestResultByCode(code)
    }
  }

  function getTestResultByCode(inputCode){
    console.log("GET TEST RESULTS")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            if(jsonData != false){
                download("TestResult.txt", jsonData)
            } else {
                window.alert("Test result not found");
            }
        }
    };
    xhttp.open("GET", "getTestResultByCode/?code="+inputCode+"&userID="+localStorage.getItem('currentUserID'), true);
    xhttp.send();
}

function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
  
    document.body.removeChild(element);
  }
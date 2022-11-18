serviceJsonData = {};

function getServices(){
    console.log("GET SERVICES")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            list1 = "";
            list2 = "";
            activeShow = " active show";
                
            for (var i = 0; i< jsonData.length; i++){
               sampleData = jsonData[i];
                list1 = list1 + `
                <div class="tab-pane`+activeShow+`" id="`+sampleData["name"] + sampleData["serviceID"].toString()+`">
                    <div class="row gy-4">
                        <div class="col-lg-8 details order-2 order-lg-1">
                            <h3>`+sampleData["name"]+`</h3>
                            <p class="fst-italic">`+sampleData["description"]+`</p>
                        </div>
                        <div class="col-lg-4 text-center order-1 order-lg-2">
                            <img src="`+sampleData["picture"]+`" alt="" class="img-fluid">
                        </div>
                    </div>
                </div>
                    `;
                    list2 = list2 + `
                    <li class="nav-item">
                    <a class="nav-link`+activeShow+`" data-bs-toggle="tab" href="#`+sampleData["name"] + sampleData["serviceID"].toString()+`">`+sampleData["name"]+`</a>
                    </li>
                    `;
                    activeShow="";
                }
                document.getElementById("SpecialitiesButtons").innerHTML = list2;
                document.getElementById("SpecialitiesContent").innerHTML = list1;
            serviceJsonData = jsonData;
        }
    };
    xhttp.open("GET", "getServices", true);
    xhttp.send();
}

function getDoctorsByService(){
    console.log("GET DOCTORS BY SERVICE")
    var xhttp = new XMLHttpRequest();
    let inputServiceID = document.getElementById("inputServiceID").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
        }
    };
    xhttp.open("GET", "getDoctorsByService/?serviceID="+inputServiceID, true);
    xhttp.send();
}

function getBookingsByDoctor(){
    console.log("GET BOOKINGS BY DOCTORS")
    var xhttp = new XMLHttpRequest();
    let inputDoctorID = document.getElementById("inputDoctorID").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
        }
    };
    xhttp.open("GET", "getBookingsByDoctor/?doctorID="+inputDoctorID, true);
    xhttp.send();
}

function getAvailability(){
    console.log("GET AVAILABILITY BY DOCTOR AND DATE")
    var xhttp = new XMLHttpRequest();
    let inputDoctorID = document.getElementById("inputDoctorID").value;
    let inputDate = document.getElementById("inputDate").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
        }
    };
    xhttp.open("GET", "getAvailability/?doctorID="+inputDoctorID+"&date="+inputDate, true);
    xhttp.send();
}

function getTestResultByCode(){
    console.log("GET TEST RESULTS")
    var xhttp = new XMLHttpRequest();
    let inputCode = document.getElementById("inputCode").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            download("TestResult.txt", jsonData)
            
        }
    };
    xhttp.open("GET", "getTestResultByCode/?code="+inputCode, true);
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

  function getProfileForLogin(){
    console.log("LOGIN teste 2")
    var xhttp = new XMLHttpRequest();
    let inputEmail = document.getElementById("loginEmail").value;
    let inputPassword = document.getElementById("loginPassword").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            if (jsonData == false){
                window.alert("NOT LOGGED IN!\nCheck your credentials and try again!")
            } else {
                //window.alert("SUCCESSFULY LOGGED IN!");
                localStorage.setItem('currentUserID',jsonData["userID"]);
                localStorage.setItem('currentUserEmail',jsonData["email"]);
                window.location.href = "profile";
            }
        }
    };
    em = encodeURIComponent(inputEmail);
    pass = encodeURI(inputPassword);
    xhttp.open("GET", "getProfileForLogin/?email='"+em+"'&password="+pass, true);
    xhttp.send();
  }

  function getDoctors(){
    console.log("GET DOCTORS")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);

            list1 = "";
            
            for (var i = 0; i< jsonData.length; i++){
                sampleData = jsonData[i];
                list1 = list1 + `
                <div class="col">
                    <div class="card">
                        <img src="`+sampleData["picture"]+`" style="height:200px;" alt="Parques de Diversão">
                        <div class="card-body">
                            <h6>`+sampleData["name"]+`</h6>
                            <p class="card-text">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p>
                            <div class="d-flex justify-content-between align-items-center">
                            </div>
                        </div>
                    </div>
                </div>
                `;
            }
            document.getElementById("DoctorsContainer").innerHTML = document.getElementById("DoctorsContainer").innerHTML + list1;
        }
    };
    xhttp.open("GET", "getDoctors", true);
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
  
  function postContact(){
    console.log("POST Contact")
    var xhttp = new XMLHttpRequest();
    titleStr = encodeURIComponent(document.getElementById("subject").value)
    textStr = encodeURIComponent(document.getElementById("message").value)
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    dateStr = mm + '-' + dd + '-' + yyyy;
    nameStr = document.getElementById("name").value
    emailStr = encodeURIComponent(document.getElementById("email").value)
    contactInfo = {"title": titleStr, "text": textStr, "date": dateStr, "name": nameStr, "email": emailStr};
    if(titleStr == "" || textStr == "" || dateStr == "" || nameStr == "" || emailStr == ""){
        window.alert("Please, fill in all the text fields.")
    } else {
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                window.alert("Thanks for your message!")
            }
        };
        xhttp.open("POST", "postContact/?title="+contactInfo["title"]+"&text="+contactInfo["text"]+"&date="+contactInfo["date"]+"&email="+contactInfo["email"]+"&name="+contactInfo["name"], true);
        xhttp.send();
    }
  }

  bookingInfo = {"date": "15-10-2022", "doctorID": "1", "userID": "1", "serviceID": "1"};
  function postBooking(){
    console.log("POST Booking")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //jsonData = JSON.parse(xhttp.responseText);
            console.log("DONE");
        }
    };
    xhttp.open("POST", "postBooking/?date="+bookingInfo["date"]+"&doctorID="+bookingInfo["doctorID"]+"&userID="+bookingInfo["userID"]+"&serviceID="+bookingInfo["serviceID"], true);
    xhttp.send();
  }

  function getBookingsByUser(){
    console.log("GET Bookings")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            //doctorJsonData = getDoctors();
            serviceData = {}
            for(var i = 0; i< serviceJsonData.length; i++){
                console.log("service")
                if(service[i]["serviceID"] == jsonData["serviceID"]){
                    serviceData = service
                }
            }
            console.log(serviceJsonData);
            //console.log(doctorJsonData);
            console.log(jsonData);

            list1 = "";
            
            for (var i = 0; i< jsonData.length; i++){
                sampleData = jsonData[i];
                list1 = list1 + `
                    <li class="list-group-item text-secondary"><pre>`+sampleData["date"]+`:    `+serviceData["name"]+`</pre></li>
                `;
            }
            document.getElementById("appointmentsListUser").innerHTML = list1;
        }
    };
    xhttp.open("GET", "getBookingsByUser/?userID="+localStorage.getItem('currentUserID'), true);
    xhttp.send();
  }

  function postProfile(){
    console.log("POST Profile")
    var xhttp = new XMLHttpRequest();
    nameStr = document.getElementById("registerName").value
    emailStr = document.getElementById("registerEmail").value
    passwordStr = document.getElementById("registerPassword").value
    profile ={"name": nameStr, "email": emailStr, "password": passwordStr }
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            if(jsonData == false){
                window.alert("Impossible to create profile.")
            } else {
                //window.alert("Profile created!")
                localStorage.setItem('currentUserID', jsonData[0]);
                localStorage.setItem('currentUserEmail',jsonData[1]);
                window.location.href = "profile";
            }
        }
    };
    xhttp.open("POST", "postProfile/?name="+profile["name"]+"&email="+profile["email"]+"&password="+profile["password"], true);
    xhttp.send();
  }

  function sendFile(event) {
    var file = event.target.files[0]
    var data = new FormData();
    data.append("myFile", file);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "upload/?nome="+document.getElementById("formFile").value, true); 
    xhr.upload.addEventListener("progress", updateProgress, false); 
    xhr.send(data);
  }


function updateProgress(evt){
    if(evt.loaded == evt.total) alert("Excerto enviado! Obrigado pela colaboraÃ§Ã£o");
}
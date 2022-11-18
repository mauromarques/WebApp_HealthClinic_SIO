function getServices(){
    console.log("GET SERVICES")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            list1 = "";
            
            for (var i = 0; i< jsonData.length; i++){
                sampleData = jsonData[i];
                list1 = list1 + `
                <option value="`+sampleData["serviceID"].toString()+`">`+sampleData["name"]+`</option>
                `;    
            }
            document.getElementById("Select1").innerHTML = document.getElementById("Select1").innerHTML + list1;
        }
    };
    xhttp.open("GET", "getServices", true);
    xhttp.send();
}

function getDoctorsByService(){
    console.log("GET DOCTORS BY SERVICE")
    var xhttp = new XMLHttpRequest();
    var val = document.getElementById("Select1").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            var select2 = document.getElementById("Select2");
            select2.disabled = false;
            picker = document.getElementById("picker");
            picker.disabled = true;
            btn = document.getElementById("btnSubmit");
            btn.disabled = true;
            list1 = '<option value="" selected disabled hidden>Choose here</option>';
            for (var i = 0; i< jsonData.length; i++){
                sampleData = jsonData[i];
                list1 = list1 + `
                <option value="`+sampleData["doctorID"].toString()+`">`+sampleData["name"]+` ||  Rating: `+sampleData["ratings"].toString()+`</option>
                `;    
            }
            select2.innerHTML = list1;
        }
    };
    xhttp.open("GET", "getDoctorsByService/?serviceID="+val, true);
    xhttp.send();
}

function enableDatePicker(){
    console.log("Enabled date picker")
    picker = document.getElementById("picker");
    picker.disabled = false;
}

function enableButton(){
    console.log("Enabled button")
    btn = document.getElementById("btnSubmit");
    btn.disabled = false;
}

function submitClick(){
    doctorID = document.getElementById("Select2").value;
    serviceID = document.getElementById("Select1").value;
    date = document.getElementById("picker").value;
    bookingInfo = {"date": date, "doctorID": doctorID, "userID": localStorage.getItem('currentUserID'), "serviceID": serviceID};
    console.log("Click submit");
    console.log(bookingInfo);
    postBooking();
}

  function postBooking(){
    console.log("POST Booking")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            jsonData = JSON.parse(xhttp.responseText);
            console.log(jsonData);
            if (jsonData == true){
                window.alert("Your appointment has been submitted!\nCheck your appointments in your profile!");
            } else {
                window.alert("This doctor has no availability for this day.\nChoose a different doctor or date!");
            }
        }
    };
    console.log(localStorage.getItem("currentUserEmail"));
    if (localStorage.getItem("currentUserEmail") == "undefined"){
        xhttp.open("POST", "postBooking/?date="+bookingInfo["date"]+"&doctorID="+bookingInfo["doctorID"]+"&userID="+bookingInfo["userID"]+"&serviceID="+bookingInfo["serviceID"], true);
    } else {
        xhttp.open("POST", "postBooking/?date="+bookingInfo["date"]+"&doctorID="+bookingInfo["doctorID"]+"&userID="+bookingInfo["userID"]+"&serviceID="+bookingInfo["serviceID"]+"&encryptedEmail="+encodeURIComponent(localStorage.getItem("currentUserEmail")), true);
    }
    xhttp.send();
  }

  function blockPage(){
    if(localStorage.getItem('currentUserID') == "" || localStorage.getItem('currentUserID') == null || localStorage.getItem('currentUserID') == undefined){
        document.getElementById("formContainer").innerHTML = `
            <div style="padding-top: 10rem; padding-bottom: 10rem  ;">
                <p class="text-center"> Please login before making appointments</p>
            </div>
        `;
    };
  }

function myFunction(){
    console.log("running...");
    var formdata = new FormData();

    var snn = document.getElementById("snn").value;
    var pwd = document.getElementById("pwd").value;
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var is_male = document.getElementById("male").value;
    is_male = String(is_male)
    var is_female = document.getElementById("female").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phnumber").value;


    formdata.append("snn", snn);
    formdata.append("password", pwd);
    formdata.append("firstName", fname);
    formdata.append("lastName", lname);
    formdata.append("sex", "1");
    formdata.append("phone", phone);
    formdata.append("email", email);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/user/user_signup/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}

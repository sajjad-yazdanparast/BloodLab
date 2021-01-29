

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function login(){
    var formdata = new FormData();
    var un =  document.getElementById("snn").value;
    var pw =  document.getElementById("pwd").value;
    formdata.append("username", un);
    formdata.append("password", pw);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };
    fetch("http://127.0.0.1:8000/user/login/", requestOptions)
    .then(response => {
        if (response.status == 401) {
            return -1;
        } else {
            return response.json()
        }
    })
    .then(result => {
        if (result == -1) {
            console.log("unauthorized");
            document.getElementById("not-auth").innerHTML = "Wrong username or password";
        } else {
            console.log("authorized");
            document.cookie = "access=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            setCookie("access", result.access, 1);
            setCookie("refresh", result.refresh, 1);
            console.log("cookies saved");

            location.replace("/home.html")
        }
    })
    .catch(error => console.log('error', error));
}
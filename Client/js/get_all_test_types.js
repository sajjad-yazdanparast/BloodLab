
var all_test_types = [];
var checked_tests = [];
var lab = ""

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function get_all_test_types() {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
      fetch("http://127.0.0.1:8000/order/get_or_create_testtype/", requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            for (let i = 0; i < result.length; i++) {
                all_test_types.push(result[i].name);
                var div_node = document.createElement("div");
                var input_node = document.createElement("input");
                input_node.setAttribute("type", "checkbox");
                input_node.setAttribute("onclick", "update_labs()");
                input_node.id = result[i].name;
                var label_node = document.createElement("label");
                var text_node = document.createTextNode(result[i].name);
                label_node.appendChild(text_node);
                div_node.appendChild(input_node);
                div_node.appendChild(label_node);
                document.getElementById("test-types").appendChild(div_node);
            }
        })
        .catch(error => console.log('error', error));
}

function update_labs() {

    for (let i = 0; i < all_test_types.length; i++) {
        
        if (document.getElementById(all_test_types[i]).checked) {
            checked_tests.push(all_test_types[i]);
        }
    }
    // console.log(checked_tests);
    // console.log(checked_tests.length)
    // var raw = "{\r\n    \"types\" : [\"corona\", \"urine\"]\r\n}";

    var myHeaders = new Headers();
    var access = "Bearer ";
    access += getCookie("access");
    myHeaders.append("Authorization", access);
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({"types":checked_tests});

    var requestOptions = {
    method: 'PUT',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/order/get_labs_doing_specific_tests_and_reserve/", requestOptions)
    .then(response => response.json())
    .then(result => {
        document.getElementById("labs").innerHTML = "";
        for (let i = 0; i < result.length; i++) {
            var already_there = 0;
            var all_radios = document.getElementsByName("lab-radio");
            for (let j = 0; j < all_radios.length; j++) {
                if (all_radios[j].value == result[i].name) {
                    already_there = 1;
                    break
                }
            }
            if (already_there) {
                continue
            }
            var div_node = document.createElement("div");
            var input_node = document.createElement("input");
            input_node.setAttribute("type", "radio");
            input_node.setAttribute("name", "lab-radio");
            input_node.setAttribute("value", result[i].name);
            var label_node = document.createElement("label");
            var text_node = document.createTextNode(result[i].name);
            label_node.appendChild(text_node);
            div_node.appendChild(input_node);
            div_node.appendChild(label_node);
            document.getElementById("labs").appendChild(div_node);
        }
    })
    .catch(error => console.log('error', error));
}

function set_lab() {
    var labs = document.getElementsByName("lab-radio");
    for (let i = 0; i < labs.length; i++) {
        if (labs[i].checked) {
            setCookie("lab", labs[i].value, 1);
            lab = labs[i].value;
            break;
        }   
    }
    create_order();
}

function create_order() {
    var myHeaders = new Headers();
    var access = "Bearer ";
    access += getCookie("access");
    console.log(access)
    myHeaders.append("Authorization", access);
    myHeaders.append("Content-Type", "application/json");
    var tests_tmp = []
    for (let i = 0; i < checked_tests.length; i++) {
        var tmp = {"type":checked_tests[i],"lab":lab,"result":"no ready"}
        tests_tmp.push(tmp);
    }
    var raw = JSON.stringify({"tests":tests_tmp,"status":0,"price":250000,"longitude":12.2,"latitude":1444.44});

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/order/get_or_create_order/", requestOptions)
    .then(response => response.json())
    .then(result => {
        console.log("here : " + result.id);
        setCookie("orderID", result.id, 1);
        console.log(getCookie("orderID"));
    })
    .catch(error => console.log('error', error));
}

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

function get_times() {
    var formdata = new FormData();
    var lab = getCookie("lab");
    formdata.append("lab", lab);
    console.log("lab:");
    console.log(lab);

    var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/order/get_lab_free_time_services/", requestOptions)
    .then(response => response.json())
    .then(result => {
        console.log(result)
        for (let i = 0; i < result.length; i++) {
            var div_node = document.createElement("div");
            var input_node = document.createElement("input");
            input_node.setAttribute("type", "radio");
            input_node.setAttribute("name", "time-radio");
            input_node.setAttribute("value", result[i].id);
            var label_node = document.createElement("label");
            var text_node = document.createTextNode("date: " + result[i].date + ", stime: " + result[i].stime + ", etime: " + result[i].etime);
            label_node.appendChild(text_node);
            div_node.appendChild(input_node);
            div_node.appendChild(label_node);
            document.getElementById("service-times").appendChild(div_node);
        }
    })
    .catch(error => console.log('error', error));
}

function set_time() {
    var time_radios = document.getElementsByName("time-radio");
    var order_id = getCookie("orderID");
    var time_id;
    for (let i = 0; i < time_radios.length; i++) {
        if (time_radios[i].checked) {
            time_id = time_radios[i].value;
        }
    }
    var formdata = new FormData();
    formdata.append("time_id", time_id);
    formdata.append("order_id", order_id);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/order/get_labs_doing_specific_tests_and_reserve/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}
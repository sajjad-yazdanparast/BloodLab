function get_statistics(){
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      var tmp;
      fetch("http://127.0.0.1:8000/user/statistics/", requestOptions)
        .then(response => response.json())
        .then(result => tmp = result)
        .then(tmp => {
            document.getElementById("blood_expert_num").innerHTML = tmp.blood_expert_num;
            document.getElementById("lab_num").innerHTML = tmp.lab_num;
            document.getElementById("type_num").innerHTML = tmp.type_num;
            document.getElementById("user_num").innerHTML = tmp.user_num;
        })
        .catch(error => console.log('error', error));
}
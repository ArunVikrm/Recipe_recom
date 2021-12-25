const form = document.getElementById('form_id');
const fileInput = document.querySelector(".file-input");
const formData = new FormData();

function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
var csrftoken = getToken('csrftoken')

// form.addEventListener("click", () =>{
//     fileInput.click();
//   });

fileInput.onchange = ({target})=>{
    let file = target.files;
    // for(i=0;i<file.length;i++){
    //     var reader = new FileReader();
    //     reader.onloadend = function() {
    //         base64String = reader.result.replace("data:", "")
    //             .replace(/^.+,/, "");

    //         imageBase64Stringsep = base64String;
    //         postImages(imageBase64Stringsep)
    //     }
    //     reader.readAsDataURL(file[i]);
    // }
    data = target.files[0];    
    //formData.append('file',target.files);
    //data = formData.getAll('file');
    //console.log(formData)
    postImages(data)

    
}

function postImages(file){
    var url = 'http://127.0.0.1:8000/api/postimages/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/x-www-form-urlencoded',
            'X-CSRFToken' : csrftoken,   
        },
        body: file,
        processData: false,
        contentType: false
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:',data)
    })

    // let xhr = new XMLHttpRequest();
    // xhr.open("POST", "http://127.0.0.1:8000/api/postimages/");
    // xhr.setRequestHeader("X-CSRFToken", csrftoken);
    // xhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
    // var fd = new FormData()
    // fd.append('file',file);
    //xhr.send(fd);
}

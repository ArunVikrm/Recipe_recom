const form = document.querySelector("form"),
fileInput = document.querySelector(".file-input"),
progressArea = document.querySelector(".progress-area"),
uploadedArea = document.querySelector(".uploaded-area");

var e = document.getElementById("ddlViewBy");

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

form.addEventListener("click", () =>{
  fileInput.click();
});
fileInput.onchange = ({target})=>{
  let file = target.files[0];
  if(file){
    let fileName = file.name;
    if(fileName.length >= 12){
      let splitName = fileName.split('.');
      fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
    }
    uploadFile(fileName,file);
  //  previewFile(file);
  }
}
function uploadFile(name,file){
  let xhr = new XMLHttpRequest();
  xhr.open("POST", "http://127.0.0.1:8000/api/postimages/");
  xhr.setRequestHeader("X-CSRFToken", csrftoken);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.upload.addEventListener("progress", ({loaded, total}) =>{
    let fileLoaded = Math.floor((loaded / total) * 100);
    let fileTotal = Math.floor(total / 1000);
    let fileSize;
    (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024*1024)).toFixed(2) + " MB";
    let progressHTML = `<li class="row">
                          <i class="fas fa-file-alt"></i>
                          <div class="content">
                            <div class="details">
                              <span class="name">${name} • Uploading</span>
                              <span class="percent">${fileLoaded}%</span>
                            </div>
                            <div class="progress-bar">
                              <div class="progress" style="width: ${fileLoaded}%"></div>
                            </div>
                          </div>
                        </li>`;
    uploadedArea.classList.add("onprogress");
    progressArea.innerHTML = progressHTML;
    if(loaded == total){
      progressArea.innerHTML = "";
      let uploadedHTML = `<li class="row">
                            <div class="content upload">
                              <i class="fas fa-file-alt"></i>
                              <div class="details">
                                <span class="name">${name} • Uploaded</span>
                                <span class="size">${fileSize}</span>
                              </div>
                            </div>
                            <i class="fas fa-check"></i>
                          </li>`;
      uploadedArea.classList.remove("onprogress");
      uploadedArea.insertAdjacentHTML("afterbegin", uploadedHTML);
    }
  });
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  var strUser = e.options[e.selectedIndex].text;
  let data = new FormData();
  data.append('category',JSON.stringify(strUser));
  data.append('file',file);
  xhr.send(data);
}

// function previewFile() {
//   const preview = document.querySelector('img');
//   const file = document.querySelector('input[type=file]').files[0];
//   const reader = new FileReader();

//   reader.addEventListener("load", function () {
//     // convert image file to base64 string
//     preview.src = reader.result;
//   }, false);

//   if (file) {
//     reader.readAsDataURL(file);
//   }
// }
// files taken via camera
var input_cam = document.querySelector('.file-cam'); 
var box = document.querySelector('.img-box');

          input_cam.onchange = function () {
            var file = input_cam.files[0];
            box.classList.add('.active');
            uploadcam(file);
            displayAsImage(file); 
          };

          function uploadcam(file) {
            var form = new FormData(),
                xhr = new XMLHttpRequest();

            form.append('image', file);
            xhr.open('post', 'xyz.django', true);
            xhr.send(form);
          }

           function displayAsImage(file) {
            var imgURL = URL.createObjectURL(file),
                img = document.createElement('img');

            img.onload = function() {
              URL.revokeObjectURL(imgURL);
            };

            img.src = imgURL;
            box.appendChild(img);
          }
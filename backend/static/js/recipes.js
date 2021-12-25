buildList()
 
 function buildList(){
     var wrapper = document.getElementById('list-wrapper');
     var url = 'http://127.0.0.1:8000/api/getRecom/' // url of the json response
 
     fetch(url)
     .then((resp) => resp.json())
     .then(function(data){
         var list = data
         for(var i in list){
 
             var item = `
                 <div class ="data-row">
                     <div class="container">
                         <h1> ${list[i].name}</h1>
                         <p>Ingredients: ${list[i].ingredients}</p>
                         <p>Diet : ${list[i].diet} </p>
                         <p>Preparation time: ${list[i].prep_time} mins </p>
                         <p>Cooking time:  ${list[i].cook_time} mins </p>
                         <p>Flavor: ${list[i].flavor_profile} </p>
                         <p>Course: ${list[i].course} </p>
                         <p>State: ${list[i].state} </p>
                         <p>Region: ${list[i].region} </p>
                         </div>
                         </div>
             `
             wrapper.innerHTML += item

        }
    })
}


// top button
var tbtn = document.getElementById("topbtn");
window.addEventListener("scroll", () => {
    if(window.pageYOffset >100){
        tbtn.style.opacity = "1";
    }
    else{
        tbtn.style.opacity = "0";
    }
}, true)
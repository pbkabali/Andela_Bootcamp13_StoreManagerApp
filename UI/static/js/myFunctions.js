
function loginCheckBox(){

    var x = document.getElementsByTagName("form")[0].getAttribute("action");
    
    if (x == "profile.html"){
        document.getElementsByTagName("form")[0].setAttribute("action", "admin_profile.html");
    }
    else{
        document.getElementsByTagName("form")[0].setAttribute("action", "profile.html");
    }
   
}

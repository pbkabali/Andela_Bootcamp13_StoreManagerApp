
function loginCheckBox(){

    var x = document.getElementsByTagName("form")[0].getAttribute("action");
    
    if (x == "inventory.html"){
        document.getElementsByTagName("form")[0].setAttribute("action", "admin_inventory.html");
    }
    else{
        document.getElementsByTagName("form")[0].setAttribute("action", "inventory.html");
    }
   
}

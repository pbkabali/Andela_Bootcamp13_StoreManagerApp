// let next_page = "profile.html";

function loginCheckBox(){

    let x = document.getElementsByTagName("form")[0].getAttribute("action");
    
    if (x == "profile.html"){
        document.getElementsByTagName("form")[0].setAttribute("action", "admin_profile.html");
    }
    else{
        document.getElementsByTagName("form")[0].setAttribute("action", "profile.html");
    }    
    
    // if (next_page == "profile.html"){
    //     next_page =  "admin_profile.html";
    // }
    // else{
    //     next_page =  "profile.html";
    // }
}

let submit = document.getElementById('submit-login'),
    url = 'https://polos-store-manager.herokuapp.com/api/v1/auth/login';


if(submit){
    submit.addEventListener("click", loginUser);
  }    

function loginUser(e){
    e.preventDefault();
    const username = document.getElementById('username').value,    
        password = document.getElementById('password').value;
        next_page = document.getElementsByTagName("form")[0].getAttribute("action")  
    if (username == "" || password == ""){
        alert("Fields cannot be blank!");
    }
    else{

   
        fetch(url, {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                username : username,
                password : password
            })
        })
        .then((res) => res.json())
        .then(data => {
            
            if (data.Response == "Welcome! successfully logged in as admin"
                && next_page == "admin_profile.html"){ 
                document.getElementsByTagName("form")[0].submit();
                localStorage.setItem('token', data.access_token);
                localStorage.setItem('message', data.Response);
                localStorage.setItem('user', username);
            }
            else if (data.Response == "Welcome! Successfully logged in!" 
                && next_page == "profile.html"){ 
                document.getElementsByTagName("form")[0].submit();
                localStorage.setItem('token', data.access_token);
                localStorage.setItem('message', data.Response);
                localStorage.setItem('user', username);
                let initialCart = [];
                localStorage.setItem('shoppingCart', JSON.stringify(initialCart));
            }            
            else if (data.Response == "incorrect password!"){
                alert("Incorrect password!");                  
            }
            else {
                alert("Account not found!");                 
            }
        }) 
    }      
}
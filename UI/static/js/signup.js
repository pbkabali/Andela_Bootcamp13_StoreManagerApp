let submit = document.getElementById('submit-signup'),
    url = 'https://polos-store-manager.herokuapp.com/api/v1/auth/signup';

submit.addEventListener("click", registerUser);    

function registerUser(){
    let firstName = document.getElementById('first-name').value,
        lastName = document.getElementById('last-name').value,
        username = document.getElementById('username').value,
        password = document.getElementById('password').value,    
        confirmPassword = document.getElementById('confirm-password').value;

    if (password == confirmPassword){    
    
    
        fetch(url, {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                first_name: firstName,
                last_name : lastName,
                username : username,
                password : password
            })
        })
        .then((res) => res.json())
        .then(data => {
            if (data.access_token){ 
                alert(data.Response +"\n Please login with your details");           
                redirect: window.location.replace("index.html");
                // localStorage.setItem('token', data.access_token)
            }
            else{
                alert(data.response);
                console.log(data);
            }
        })
    }   
    else{
        alert("Passwords do not match!");
    }
}




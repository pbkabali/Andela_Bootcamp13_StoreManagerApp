let submit = document.getElementById('submit-product'),
    url = 'https://polos-store-manager.herokuapp.com/api/v1/products/create';


if(submit){
    submit.addEventListener("click", createProduct);
  }    

function createProduct(e){
    e.preventDefault();
    const category = document.getElementById('category').value,    
        name = document.getElementById('name').value,
        quantity = parseInt(document.getElementById('quantity').value),
        unit = document.getElementById('unit').value,
        price = parseFloat(document.getElementById('price').value),
        minimumStock = parseInt(document.getElementById('minimum-stock').value);
    if (category == "" || name == "" || quantity == "" 
        || unit == "" || price == "" || minimumStock == ""){
        alert("Fields cannot be blank!");
    }
    else{

   
        fetch(url, {
            method: "POST",
            headers: {  
                'Content-Type': 'application/json',            
                'Authorization': 'Bearer '+ localStorage.getItem('token')
            },
            body: JSON.stringify({
                category : category,
                name : name,
                unit : unit,
                unit_price : price,
                quantity : quantity,
                minimum_quantity : minimumStock
            })
        })
        .then((res) => res.json())
        .then(data => {
            
            if (data.product_added){ 
                document.getElementsByTagName("form")[0].submit();               
            }            
            else if (data.response){
                alert(data.response);                  
            }
            else {
                alert("Error creating product!");                 
            }
            // console.log(data);
        }) 
    }      
}
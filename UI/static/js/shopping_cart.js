window.onload = function() {
    const shoppingCart = JSON.parse(localStorage.getItem("shoppingCart"));
        shopping_cart_table = document.getElementById('shopping-cart-table')       

    let table_contents = `
    <tr>
        <th>ID</th>
        <th>Item</th>
        <th>Quantity</th>
        <th>Amount</th>
        <th></th>
    </tr>
    `,
    totalPrice = 0;
    shoppingCart.forEach(product => {
        table_contents +=`
        <tr> 
            <td>${product.product_id}
            </td>
            <td>${product.product_name}
            </td>
            <td>${product.quantity}
            </td>
            <td>${product.amount}
            </td>  
            <td><button class= "button1">Remove</button>
            </td>                    
        </tr>
        `;   
        totalPrice += product.amount;         
    });
    shopping_cart_table.innerHTML = table_contents;
    document.getElementById('total-price').innerHTML = totalPrice;    
}
const createSaleBtn = document.getElementById('create-record'),
    addMoreItemsBtn = document.getElementById('add-more-items'),
    emtpyCartBtn = document.getElementById('empty-cart');

createSaleBtn.addEventListener('click', createRecord);

function createRecord(){
    let url = 'https://polos-store-manager.herokuapp.com/api/v1/sales/create_record'

    fetch(url, {
        method: "POST",
        headers: {  
            'Content-Type': 'application/json',            
            'Authorization': 'Bearer '+ localStorage.getItem('token')
        },
        body: localStorage.getItem("shoppingCart")
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.created_record){
            document.getElementById('sale-response').innerHTML="Sale record created successfully by:";
            document.getElementById('id-tag').innerHTML="Attendant ID: "+ data.created_record[0].attendant_id;
            document.getElementById('name-tag').innerHTML="Attendant Name: "+ data.created_record[1].attendant_name;
            createSaleBtn.parentNode.removeChild(createSaleBtn);
            addMoreItemsBtn.parentNode.removeChild(addMoreItemsBtn);
            emtpyCartBtn.parentNode.removeChild(emtpyCartBtn);
            document.getElementById('exit-sale').innerHTML="OK";
            localStorage.setItem("shoppingCart", JSON.stringify([]));
        }
        else {
            alert(data.response);
        }
    })
}    



window.onload = function() {
    const products_table = document.getElementById('products_table'),
        products_url = 'https://polos-store-manager.herokuapp.com/api/v1/products';

    fetch(products_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {
        let table_contents = `
        <tr> 
        <th>ID</th>                               
        <th>Product Category</th>
        <th>Product Name</th>
        <th>Quantity in Stock</th>
        <th>Unit Price</th>
        <th>Add to Cart</th>       
        </tr>
        `;
        data.available_products.forEach(product => {
            table_contents +=`
            <tr> 
                <td data-id = "${product.product_id}" 
                    onclick = "productDetails(this)">${product.product_id}
                </td>                               
                <td data-id = "${product.product_id}" 
                    onclick = "productDetails(this)">${product.category}
                </td>
                <td data-id = "${product.product_id}" 
                    onclick = "productDetails(this)">${product.product_name}
                </td>
                <td data-id = "${product.product_id}" 
                    onclick = "productDetails(this)">${product.quantity}
                </td>
                <td data-id = "${product.product_id}" 
                    onclick = "productDetails(this)">${product.unit_price}
                </td>  
                <td>
                    <input type="checkbox" class = "checkbox1" 
                    data-id = "${product.product_id}" data-name = "${product.product_name}"
                    data-price = "${product.unit_price}" onclick = "addToCart(this)"></input>
                </td>                                     
            </tr>
            `;            
        });
        products_table.innerHTML = table_contents;
    })
}
function productDetails(e){   
let productId = e.getAttribute('data-id'),
    single_product_url = 'https://polos-store-manager.herokuapp.com/api/v1/products/'+productId;

fetch(single_product_url, {
    headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {
        let product_details = `
        <h2 class = "form-heading">PRODUCT DETAILS</h2>
        <br>
        <table class = "table1">                                                        
                
            <tr>
                <th>Detail</th>
                <th>Value</th>                           
            </tr>
            <tr>               
                <td>product ID</td>
                <td>${data.found_product.product_id}</td>                 
            </tr>    
            <tr>               
                <td>Product Name</td>
                <td>${data.found_product.product_name}</td>                 
            </tr>   
            <tr>               
                <td>Quantity in Stock</td>
                <td>${data.found_product.quantity}</td>                 
            </tr>  
            <tr>               
                <td>Unit Price</td>
                <td>${data.found_product.unit_price}</td>                 
            </tr>  
            <tr>               
                <td>Unit of measure</td>
                <td>${data.found_product.unit}</td>                 
            </tr>   
            <tr>               
                <td>Minimum Allowed quantity</td>
                <td>${data.found_product.minimum_quantity}</td>                 
            </tr>
        </table> 
        <br>
        <br>
        <a href = "inventory.html">Back to All products</a>
        <br>
        <br>                     
        `;
        document.getElementById('form-div').innerHTML = product_details;
        
    })  
}

function addToCart(e){
    let productId = parseInt(e.getAttribute('data-id')),
        quantity = parseInt(prompt("Enter quantity to add", 1)),
        unit_price = parseFloat(e.getAttribute('data-price')),
        productName = e.getAttribute('data-name'),
        amount = quantity*unit_price,
        saleDetail = {"product_id":productId, "quantity":quantity,
            'product_name':productName, "amount": amount
        },         

        oldCart = JSON.parse(localStorage.getItem('shoppingCart'));
    oldCart.push(saleDetail);
    localStorage.setItem('shoppingCart', JSON.stringify(oldCart));
}

// onclick = "addToCart(this)"
// onclick = "productDetails(this)"


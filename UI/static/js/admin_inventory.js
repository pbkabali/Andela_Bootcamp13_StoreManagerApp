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
       
        </tr>
        `;
        data.available_products.forEach(product => {
            table_contents +=`
            <tr data-id = "${product.product_id}" onclick = "productDetails(this)"> 
                <td id = "product-category">${product.product_id}</td>                               
                <td id = "product-category">${product.category}</td>
                <td id = "item-name">${product.product_name}</td>
                <td id = "item-quantity">${product.quantity}</td>
                <td id = "item-unitprice">${product.unit_price}</td>
                                       
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
            <a href = "admin_inventory.html">Back to All products</a>
            <br>
            <br>                     
            `;
            document.getElementById('form-div').innerHTML = product_details;
           
        })  
}


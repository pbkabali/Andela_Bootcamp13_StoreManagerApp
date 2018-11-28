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
        <th>Edit Product</th>
        </tr>
        `;
        data.available_products.forEach(product => {
            table_contents +=`
            <tr> 
                <td id = "product-category">${product.product_id}</td>                               
                <td id = "product-category">${product.category}</td>
                <td id = "item-name">${product.product_name}</td>
                <td id = "item-quantity">${product.quantity}</td>
                <td id = "item-unitprice">${product.unit_price}</td>
                <td><button class= "button3">Edit/Delete</button></td>                           
            </tr>
            `;            
        });
        products_table.innerHTML = table_contents;
    })
  }



window.onload = function() {
    const all_sales_table = document.getElementById('all-sales-table'),
        all_sales_url = 'https://polos-store-manager.herokuapp.com/api/v1/admin/sales/all';

    fetch(all_sales_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {
        let table_contents = `
        <tr>
            <th>ID</th>
            <th>Date of Sale</th>
            <th>Attendant ID</th> 
            <th>Product Name</th>                           
            <th>Quantity Sold</th>
            <th>Total Price</th>                 
        </tr>
        `;
        data.sales_records.forEach(record => {
            table_contents +=`
            <tr>
                <td id = "date-of-sale">${record.sale_id}</td>
                <td id = "date-of-sale">${record.created_at}</td>
                <td id = "id-number">${record.attendant_id}</td>  
                <td id = "product-name">${record.product_name}</td>    
                <td id = "quantity">${record.quantity}</td> 
                <td id = "amount">${record.total_price}</td>                                                                      
            </tr>     
            `;            
        });
        all_sales_table.innerHTML = table_contents;
    })
  }



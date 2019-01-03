window.onload = function() {
    const 
        individual_sales_url = 'https://polos-store-manager.herokuapp.com//api/v1/sales/personal';

    fetch(individual_sales_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {                 
        let total_products = 0,
            total_records = 0,
            total_revenue = 0,
            table_contents = `
        <tr>
            <th>ID</th>
            <th>Date of Sale</th>
            <th>Attendant ID</th> 
            <th>Product Name</th>                           
            <th>Quantity Sold</th>
            <th>Total Price</th>                 
        </tr>
        `;
        data.your_records.forEach(record => {
            // if (record.cancelled == false){            
                total_products += record.quantity;
                total_records++;
                total_revenue += record.total_price;
                table_contents +=`
                <tr> 
                    <td>${record.sale_id}</td>
                    <td>${record.created_at}</td>
                    <td>${record.attendant_id}</td>  
                    <td>${record.product_name}</td>    
                    <td>${record.quantity}</td> 
                    <td>${record.total_price}</td> 

                </tr>     
                `;                   
            // }
        });
        document.getElementById("ind-sales-table").innerHTML = table_contents; 
        document.getElementById('total-records').innerHTML = total_records; 
        document.getElementById('total-products').innerHTML = total_products; 
        document.getElementById('total-revenue').innerHTML = total_revenue;     
        
    })
}  
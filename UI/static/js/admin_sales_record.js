const all_sales_table = document.getElementById('all-sales-table');
window.onload = function() {
    const 
        all_sales_url = 'https://polos-store-manager.herokuapp.com/api/v1/admin/sales/all';

    fetch(all_sales_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {          
        localStorage.setItem('salesData', JSON.stringify(data));        
    })
}  


document.getElementById("submit-id").addEventListener('click', individualRecord);
const ind_sales_table = document.getElementById('ind-sales-table');

function individualRecord(e){
    e.preventDefault();
    let sales = JSON.parse(localStorage.getItem('salesData')),
        attendantId = parseInt(document.getElementById("attendant-id").value),
        total_products = 0,
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
    sales.sales_records.forEach(record => {
        if (record.attendant_id == attendantId && record.cancelled == false){
        
            total_products += record.quantity;
            total_records++;
            total_revenue += record.total_price;
            table_contents +=`
            <tr onclick="recordDetails(this)" data-id ="${record.sale_id}"> 
                <td onclick="tag()">${record.sale_id}</td>
                <td>${record.created_at}</td>
                <td>${record.attendant_id}</td>  
                <td>${record.product_name}</td>    
                <td>${record.quantity}</td> 
                <td>${record.total_price}</td> 

            </tr>     
            `;   
            document.getElementById('attendant-name').innerHTML = `Attendant's Name: <span class = "totals1" >${record.attendant_name}</span>`;
        }
    });
    ind_sales_table.innerHTML = table_contents; 
    document.getElementById('total-records').innerHTML = `Total Records: <span class = "totals1" > ${total_records}</span>`; 
    document.getElementById('total-products').innerHTML = `Total items sold: <span class = "totals1" > ${total_products}</span>`; 
    document.getElementById('total-revenue').innerHTML = `Total Amount Generated:<span class = "totals2" > ${total_revenue}</span>`;        
}

function recordDetails(e){   
    let saleId = e.getAttribute('data-id'),
        single_sale_url = 'https://polos-store-manager.herokuapp.com/api/v1/sales/'+saleId;

    fetch(single_sale_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
        })
        .then((res) => res.json())
        .then((data) => {
            let sale_details = `
            <h2 class = "form-heading">DETAILS OF SALE</h2>
            <br>
            <table class = "table1">                                                        
                    
                <tr>
                    <th>Detail</th>
                    <th>Value</th>                           
                </tr>
                <tr>               
                    <td>Sale-ID</td>
                    <td>${data.found_record.sale_id}</td>                 
                </tr>     
                <tr>               
                    <td>Sale Date</td>
                    <td>${data.found_record.created_at}</td>                 
                </tr>   
                <tr>               
                    <td>Product ID</td>
                    <td>${data.found_record.product_id}</td>                 
                </tr>     
                <tr>               
                    <td>Product Name</td>
                    <td>${data.found_record.product_name}</td>                 
                </tr>   
                <tr>               
                    <td>Quantity Sold</td>
                    <td>${data.found_record.quantity}</td>                 
                </tr>  
                <tr>               
                    <td>Unit Price</td>
                    <td>${data.found_record.unit_price}</td>                 
                </tr>  
                <tr>               
                    <td>Total Price</td>
                    <td>${data.found_record.total_price}</td>                 
                </tr>   
                <tr>               
                    <td>Attendant-ID</td>
                    <td>${data.found_record.attendant_id}</td>                 
                </tr>
                <tr>               
                    <td>Attendant's Name</td>
                    <td>${data.found_record.attendant_name}</td>                 
                </tr>
            </table> 
            <br>
            <br>
            <a href = "admin_sales_record.html">Back</a>            
            <br>
            <br>
            <button class= "button2" onclick="reverseSale(this)" data-id ="${data.found_record.sale_id}">Reverse sale</button>
            <br>   
            <br>                   
            `;
            document.getElementById('form-div').innerHTML = sale_details;            
        })  
}

function reverseSale(e){    
    let saleId = e.getAttribute('data-id'),
        reverse_sale_url = 'https://polos-store-manager.herokuapp.com/api/v1/sales/cancel/'+saleId;

    fetch(reverse_sale_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
        })
        .then((res) => res.json())
        .then((data) => {
            alert(data.response);
            redirect: window.location.replace("admin_sales_record.html");
        })
}        
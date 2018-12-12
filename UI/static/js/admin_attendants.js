const all_attendants_table = document.getElementById('all-attendants-table');
window.onload = function() {
    const 
        all_attendants_url = 'https://polos-store-manager.herokuapp.com/api/v1/auth/users';

    fetch(all_attendants_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {
        let table_contents = `
        <tr>       
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Permissions</th>
        <th>Edit/Delete <br>Attendant</th>          
        </tr>
        `;
        data.available_users.forEach(record => {
            
            table_contents +=`
            <tr onclick="attendantDetails(this)" data-id ="${record.users_id}"> 
                <td>${record.users_id}</td>
                <td>${record.first_name}</td>
                <td>${record.last_name}</td> 
                <td>${record.role}</td> 
                <td><button class= "button3">Edit/Delete</button></td>
            </tr>     
            `;              
        });
        all_attendants_table.innerHTML = table_contents;                
    })
  }  


// function recordDetails(e){   
//     let saleId = e.getAttribute('data-id'),
//         single_sale_url = 'https://polos-store-manager.herokuapp.com/api/v1/sales/'+saleId;

//     fetch(single_sale_url, {
//         headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
//         })
//         .then((res) => res.json())
//         .then((data) => {
//             let sale_details = `
//             <h2 class = "form-heading">DETAILS OF SALE</h2>
//             <br>
//             <table class = "table1">                                                        
                    
//                 <tr>
//                     <th>Detail</th>
//                     <th>Value</th>                           
//                 </tr>
//                 <tr>               
//                     <td>Sale-ID</td>
//                     <td>${data.found_record.sale_id}</td>                 
//                 </tr>     
//                 <tr>               
//                     <td>Sale Date</td>
//                     <td>${data.found_record.created_at}</td>                 
//                 </tr>   
//                 <tr>               
//                     <td>Product ID</td>
//                     <td>${data.found_record.product_id}</td>                 
//                 </tr>     
//                 <tr>               
//                     <td>Product Name</td>
//                     <td>${data.found_record.product_name}</td>                 
//                 </tr>   
//                 <tr>               
//                     <td>Quantity Sold</td>
//                     <td>${data.found_record.quantity}</td>                 
//                 </tr>  
//                 <tr>               
//                     <td>Unit Price</td>
//                     <td>${data.found_record.unit_price}</td>                 
//                 </tr>  
//                 <tr>               
//                     <td>Total Price</td>
//                     <td>${data.found_record.total_price}</td>                 
//                 </tr>   
//                 <tr>               
//                     <td>Attendant-ID</td>
//                     <td>${data.found_record.attendant_id}</td>                 
//                 </tr>
//                 <tr>               
//                     <td>Attendant's Name</td>
//                     <td>Name</td>                 
//                 </tr>
//             </table> 
//             <br>
//             <br>
//             <a href = "admin_overall_sales.html">Back to All sales</a>
//             <br>
//             <br>                     
//             `;
//             document.getElementById('form-div').innerHTML = sale_details;            
//         })  
// }







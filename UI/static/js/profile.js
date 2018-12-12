window.onload = function() {
    document.getElementById("names-of-user").innerHTML
    = localStorage.getItem('user');
    const 
        personal_sales_url = 'https://polos-store-manager.herokuapp.com/api/v1/sales/personal';

    fetch(personal_sales_url, {
        headers: {'Authorization': 'Bearer '+ localStorage.getItem('token')}
    })
    .then((res) => res.json())
    .then((data) => {
        let total_products = 0,
            total_records = 0,
            total_revenue = 0;            
        data.your_records.forEach(record => {
            total_products += record.quantity;
            total_records++;
            total_revenue += record.total_price; 
        });        
        document.getElementById('total-records').innerHTML = total_records; 
        document.getElementById('total-products').innerHTML = total_products; 
        document.getElementById('total-revenue').innerHTML = total_revenue;       
    })
  }
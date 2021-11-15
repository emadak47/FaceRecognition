function changeFont(){
  let y = document.getElementById("minDate");
  y.type = "date";
  y.style = "font-size: 10px"
  let x = document.getElementById("maxDate");
  x.type = "date";
  x.style = "font-size: 10px"
}

function addTransaction(businessType, merchantName, amount){
  document.getElementById('transactionTable').innerHTML +=
  `<tr>
        <th scope="row">` + businessType + `</th>
        <td>` + merchantName + `</td>
        <td>-` + amount + ` HKD</td>
    </tr>`;
}
window.onload= function(){

  let y = document.getElementById("minDate");
  y.onfocus=changeFont;
  let x = document.getElementById("maxDate");
  x.onfocus=changeFont;

  document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault(); // prevent submission of the form
    let elementsHTML = document.querySelector('form').elements;
    console.log(elementsHTML)
  });



  fetch('/transactionsBackend')
    .then(function (response) {
        return response.json();
    }).then(function (rows) {
        console.log('GET response:');
        console.log(rows.data);
        rows = rows.data;
        for (var i = 0; i < rows.length; i++) { //iterate through response
          console.log("Merchant ID" + rows[i]["merchant_id"] + " Amount: " + rows[i]["amount"]);
          addTransaction(rows[i]["merchant_id"], rows[i]["merchant_id"], rows[i]["amount"])
        }


    });

}

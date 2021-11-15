function changeFont(){
  let y = document.getElementById("minDate");
  y.type = "date";
  y.style = "font-size: 10px"
  let x = document.getElementById("maxDate");
  x.type = "date";
  x.style = "font-size: 10px"
}

function replaceTransactions(rows){
  rows = rows.data;
  document.getElementById('transactionTable').innerHTML = "" //reset innerHTML
  for (var i = 0; i < rows.length; i++) { //iterate through response
    businessType = rows[i]["business_type"]; merchantName = rows[i]["name"]; amount = rows[i]["amount"];
    document.getElementById('transactionTable').innerHTML +=
    `<tr>
          <th scope="row">` + businessType + `</th>
          <td>` + merchantName + `</td>
          <td>` + amount + ` HKD</td>
      </tr>`;
  }
}

function getTransactions(customer_id){
  // e.preventDefault(); // prevent submission of the form REMOVE THIS
  let elementsHTML = document.querySelector('form').elements;

  //fetch vlaues from form and set default values below if not set by user
  if (!(parseInt(document.getElementById("minAmount").value))) minAmount = -1
  else minAmount = parseInt(document.getElementById("minAmount").value)
  if (!(parseInt(document.getElementById("maxAmount").value))) maxAmount = 99999999
  else maxAmount = parseInt(document.getElementById("maxAmount").value)
  if (!(document.getElementById("minDate").value)) minDate = "1970-01-01"
  else minDate = document.getElementById("minDate").value
  if (!(document.getElementById("maxDate").value)) maxDate = "2022-01-01"
  else maxDate = document.getElementById("maxDate").value
  account = document.getElementById("accountsDropdown").selectedOptions[0].value;

  formData = {
    "minAmount":minAmount,
    "maxAmount":maxAmount,
    "minDate":minDate,
    "maxDate":maxDate,
    "account":account,
  }
  console.log(formData)
  let url = '/transactionsBackend/' + customer_id;
  fetch(url,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: JSON.stringify(formData)
  })
  .then(function (response) {
        return response.json();
    }).then(function (rows) {
        replaceTransactions(rows);
    });
}

function getAccounts(customer_id){
  let url = '/getAccounts/' + customer_id;
  let dropdown = document.getElementById("accountsDropdown");
  fetch(url,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    }
  })
  .then(function (response) {
        return response.json();
    }).then(function (result) {
      accounts = result["data"]
      for (var i = 0; i < accounts.length; i++) {
        dropdown.innerHTML+=
        `<option value=` + accounts[i]["account_no"]+ `> Account #`+ accounts[i]["account_no"] + ` (`+ accounts[i]["Account_type"] + `)</option>`
      }
    });
}
window.onload= function(){
  let customer_id = window.location.pathname.match('[0-9]+$')[0]

  let y = document.getElementById("minDate");
  y.onfocus=changeFont;
  let x = document.getElementById("maxDate");
  x.onfocus=changeFont;

  getAccounts(customer_id);


  document.querySelector('form').addEventListener('submit', function(e){
    e.preventDefault();
    getTransactions(customer_id);
  } );


  getTransactions(customer_id);
}

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
    date = rows[i]["creation_date"]; time = rows[i]["creation_time"]; description = rows[i]["description"];
    if (!(description)){ description = ""}
    icon = {"Food":"cutlery", "Entertainment":"ticket", "Education":"graduation-cap", "Transportation":"subway", "Medical":"plus-square",  }[businessType]
    document.getElementById('transactionTable').innerHTML +=
    `<tr>
          <th scope="row" style="text-align:center"> <i class="fa fa-` + icon + `"></i> </th>
          <td>` + merchantName + `</td>
          <td style="width:90px">` + date + `</td>
          <td>` + time + `</td>
          <td>` + description + `</td>
          <td style="width:80px">` + amount + ` HKD</td>
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
  if (!(document.getElementById("minTime").value)) minTime = "00:00:00"
  else minTime = (document.getElementById("minTime").value + ':00')
  if (!(document.getElementById("maxTime").value)) maxTime = "23:59:00"
  else maxTime = (document.getElementById("maxTime").value + ':00')
  account = document.getElementById("accountsDropdown").selectedOptions[0].value;

  formData = {
    "minAmount":minAmount,
    "maxAmount":maxAmount,
    "minDate":minDate,
    "maxDate":maxDate,
    "account":account,
    "minTime":minTime,
    "maxTime":maxTime
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
      dropdown.innerHTML += `<option id = "All" selected value="All">All</option>`
      accounts = result["data"]
      for (var i = 0; i < accounts.length; i++) {
        dropdown.innerHTML+=
        `<option id="account_`+accounts[i]["account_no"] + `" value=` + accounts[i]["account_no"]+ `> Account #`+ accounts[i]["account_no"] + ` (`+ accounts[i]["Account_type"] + `)</option>`
      }
    });
}

function accountPreselection(customer_id){
  //Account pre-selection logic
  if (window.location.search != ""){
    account_no = window.location.search.match('[0-9]+$')[0]
    console.log("Show account #" + account_no)
    window.history.pushState("", "", '/transactions/' + customer_id);
    console.log("account_" + account_no)
    let option = document.getElementById("account_" + account_no)
    option.selected = true;
  }
  else{
    console.log("no account pre-selected")
  }

}

function waitForElementToDisplay(selector, callback, checkFrequencyInMs, timeoutInMs) {
  var startTimeInMs = Date.now();
  (function loopSearch() {
    if (document.querySelector(selector) != null) {
      callback();
      return;
    }
    else {
      setTimeout(function () {
        if (timeoutInMs && Date.now() - startTimeInMs > timeoutInMs)
          return;
        loopSearch();
      }, checkFrequencyInMs);
    }
  })();
}

window.onload= function(){
  let y = document.getElementById("minDate");
  y.onfocus=changeFont;
  let x = document.getElementById("maxDate");
  x.onfocus=changeFont;

  var customer_id = window.location.pathname.match('[0-9]+$')[0]

getAccounts(customer_id)
 waitForElementToDisplay("#All",function(){accountPreselection(customer_id); getTransactions(customer_id);
},100,9000);

  document.querySelector('form').addEventListener('submit', function(e){
    e.preventDefault();
    getTransactions(customer_id);
  } );


}

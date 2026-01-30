async function loadOrderbook() {
    const res = await fetch("/orderbook");
    const data = await res.json();
  
    const tbody = document.getElementById("orders");
    tbody.innerHTML = "";
  
    data.buy.forEach(o => {
      tbody.innerHTML += `
        <tr>
          <td class="buy">BUY</td>
          <td>${o.price}</td>
          <td>${o.qty}</td>
        </tr>`;
    });
  
    data.sell.forEach(o => {
      tbody.innerHTML += `
        <tr>
          <td class="sell">SELL</td>
          <td>${o.price}</td>
          <td>${o.qty}</td>
        </tr>`;
    });
  }
  
  async function startStrategy() {
    await fetch("/start_strategy");
  }
  
  async function stopStrategy() {
    await fetch("/stop_strategy");
  }
  
  setInterval(loadOrderbook, 1000);
  
async function loadOrderbook() {
    const res = await fetch("/orderbook");
    const data = await res.json();
    let html = `<table><tr><th>Side</th><th>Price</th><th>Qty</th></tr>`;
    for (let side in data) {
      data[side].forEach(order => {
        html += `<tr><td>${side}</td><td>${order.price}</td><td>${order.qty}</td></tr>`;
      });
    }
    html += `</table>`;
    document.getElementById("orderbook").innerHTML = html;
  }
  setInterval(loadOrderbook, 1000);
  
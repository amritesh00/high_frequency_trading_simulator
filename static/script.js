const socket = io();

socket.on("orderbook_update", data => {
    update("buy", data.buy);
    update("sell", data.sell);
});

function update(side, orders) {
    const ul = document.getElementById(side);
    ul.innerHTML = "";
    orders.forEach(o => {
        ul.innerHTML += `<li>${o.price} x ${o.qty}</li>`;
    });
}

function start() {
    fetch("/start_strategy");
}

function stop() {
    fetch("/stop_strategy");
}

function placeOrder() {
    fetch("/order", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            side: document.getElementById("side").value,
            price: document.getElementById("price").value,
            qty: document.getElementById("qty").value
        })
    });
}

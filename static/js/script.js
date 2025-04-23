const ws = new WebSocket("ws://localhost:6789");
const messages = document.getElementById("messages");
const form = document.getElementById("form");
const input = document.getElementById("input");
const user = prompt("Digite seu nome:");

ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    const item = document.createElement("div");
    item.textContent = `${msg.user}: ${msg.text}`;
    messages.appendChild(item);
    messages.scrollTop = messages.scrollHeight;
};

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const message = {
        user: user,
        text: input.value
    };
    ws.send(JSON.stringify(message));
    input.value = "";
});
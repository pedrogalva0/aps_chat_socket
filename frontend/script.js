const socket = io("http://localhost:5000"); // Altere para o endereço do backend real

let currentRoom = '';

socket.on('assign_id', (id) => {
    document.getElementById('username').value = id;
});

socket.on('user_list', (list) => {
    const ul = document.getElementById('users');
    ul.innerHTML = '';
    list.forEach(user => {
        const li = document.createElement('li');
        li.textContent = user;
        ul.appendChild(li);
    });
});

socket.on('message', (data) => {
    const messages = document.getElementById('messages');
    messages.innerHTML += `<p>${data.msg}</p>`;
});

function sendMessage() {
    const msg = document.getElementById('message').value;
    socket.emit('send_message', { msg });
    document.getElementById('message').value = '';
}

function enterRoom() {
    const room = document.getElementById('room').value;
    socket.emit('create_or_join_room', { room });
}

function setUsername() {
    const name = document.getElementById('username').value;
    socket.emit('set_username', name);
}

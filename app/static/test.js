document.addEventListener("DOMContentLoaded", (event) => {
    let chatWindow = document.getElementById('chat');
    chatWindow.scrollTop = chatWindow.scrollHeight;
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    const room = document.getElementById('recipient_id').value + '_' + document.getElementById('user_id').value;
    socket.emit('join', {'room': room});

    socket.on('receive_message', function(data) {
        let chat = document.getElementById('chat');
        let messageElement = document.createElement('li');
        messageElement.className = data.sender_id == document.getElementById('user_id').value ? 'me' : 'you';
        messageElement.innerHTML =  `
        <div class="entete">
            <span class="status ${data.sender_id == document.getElementById('user_id').value ? 'blue' : 'green'}"></span>
            <h2>${data.sender_id == document.getElementById('user_id').value ? 'you' : data.sender}</h2>
            <h3>${data.created_at}</h3>
        </div>
        <div class="triangle"></div>
        <div class="message">
            ${data.content}
        </div>
    `;
    
        chat.appendChild(messageElement);
        let chatWindow = document.getElementById('chat');
        chatWindow.scrollTop = chatWindow.scrollHeight;
    });

    socket.on('join_response', function(data) {
        console.log(data.message); // Username has joined the room roomname.
    });

    document.getElementById('send').onclick = function() {
        const message = document.getElementById('message').value;
        socket.emit('send_message', {
            content: message,
            recipient_id: document.getElementById('recipient_id').value
        });
        document.getElementById('message').value = "";
    }

    socket.on('status_update', function(data) {
        if (data.user_id == document.getElementById('recipient_id').value) {
            const statusElement = document.getElementById('active');
            statusElement.textContent = data.status.charAt(0).toUpperCase() + data.status.slice(1);
        }
    });
});    
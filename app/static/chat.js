/*let selectedUserId = null;
        const socket = io();

        $(document).ready(function() {
            $('.user-link').on('click', function(e) {
                e.preventDefault();
                selectedUserId = $(this).data('id');
                loadMessages(selectedUserId);
                socket.emit('join', {room: selectedUserId});
            });

            $('#send-btn').on('click', function() {
                const message = $('#message-input').val();
                if (message.trim() !== '' && selectedUserId !== null) {
                    socket.emit('send_message', {
                        receiver_id: selectedUserId,
                        message: message
                    });
                }
            });

            socket.on('receive_message', function(data) {
                if (data.receiver_id == selectedUserId || data.sender_id == selectedUserId) {
                    const messageElement = $('<div class="message"></div>');
                    messageElement.text(`${data.sender_id === {{ current_user.id }} ? 'You' : 'User ' + data.sender_id}: ${data.message}`);
                    $('#messages').append(messageElement);
                }
            });
        });

        function loadMessages(receiverId) {
            $.ajax({
                url: '/chat/get_messages/' + receiverId,
                method: 'GET',
                success: function(data) {
                    $('#messages').empty();
                    data.forEach(function(msg) {
                        const messageElement = $('<div class="message"></div>');
                        messageElement.text(`${msg.sender_id === {{ current_user.id }} ? 'You' : 'User ' + msg.sender_id}: ${msg.message}`);
                        $('#messages').append(messageElement);
                    });
                }
            });
        }*/
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        function sendMessage() {
            var message = document.getElementById('message').value;
            if (message.trim()) {
                socket.emit('send_message', {
                    message: message,
                    recipient_id: '{{ recipient.id }}'
                });
                document.getElementById('message').value = '';
            }
        }

        socket.on('recieve_message', function(data) {
            document.getElementById('output').innerHTML += '<p><strong>' + data.sender + ':</strong> ' + data.message + '</p>';
            var chatWindow = document.getElementById('chat-window');
            chatWindow.scrollTop = chatWindow.scrollHeight;
        });

        socket.on('connect', function() {
            socket.emit('join', {
                room: '{{ recipient.id }}_{{ user.id }}'
            });
        });
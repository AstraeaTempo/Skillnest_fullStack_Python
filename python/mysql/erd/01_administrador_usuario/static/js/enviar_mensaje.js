document.addEventListener('DOMContentLoaded', () => {
    
    // Elementos de Mensajes
    const messageInput = document.getElementById('message-input');
    const sendMessageBtn = document.getElementById('send-message');

    // Elementos de Comentarios
    const commentInput = document.getElementById('comment-input');
    const sendCommentBtn = document.getElementById('send-comment');
    const commentsList = document.getElementById('comments-list');

    // Funcionalidad básica para simular el envío de comentarios
    sendCommentBtn.addEventListener('click', () => {
        const commentText = commentInput.value.trim();
        
        if (commentText !== "") {
            // Crear el contenedor del nuevo comentario simulado
            const commentItem = document.createElement('div');
            commentItem.classList.add('comment-item');

            commentItem.innerHTML = `
                <a href="#" class="meta-link-comment">Comentario de Usuario, hace unos segundos</a>
                <p class="lorem-text text-indented">${commentText}</p>
            `;

            // Añadir a la lista
            commentsList.appendChild(commentItem);
            
            // Limpiar el input
            commentInput.value = "";
        }
    });

    // Permitir enviar el comentario también al presionar "Enter"
    commentInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendCommentBtn.click();
        }
    });

    // Simulación simple para el botón enviar mensaje principal
    sendMessageBtn.addEventListener('click', () => {
        if (messageInput.value.trim() !== "") {
            alert('Mensaje enviado: ' + messageInput.value);
            messageInput.value = "";
        }
    });
});
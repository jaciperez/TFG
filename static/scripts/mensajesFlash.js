// Para mensajes de tipo Flash
setTimeout(() => {
    const mensaje = document.querySelector('.mensaje-flash');
    if (mensaje) {
        mensaje.style.transition = 'opacity 1s ease';
        mensaje.style.opacity = '0';
        setTimeout(() => mensaje.remove(), 1000);
    }
}, 4000);

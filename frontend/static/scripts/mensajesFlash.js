// Solo ejecuta si hay un mensaje flash en pantalla
document.addEventListener('DOMContentLoaded', () => {
  const mensaje = document.querySelector('.mensaje-flash');
  if (!mensaje) return;

  // Espera 2 segundos y haz fade‐out en 0.5 s, luego elimina el nodo
  setTimeout(() => {
    mensaje.style.transition = 'opacity 0.5s ease';
    mensaje.style.opacity    = '0';
    setTimeout(() => mensaje.remove(), 500);
  }, 2000);
});

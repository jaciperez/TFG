document.addEventListener('DOMContentLoaded', () => {
  const tooltip = document.getElementById('tooltip-panel');

  document.querySelectorAll('.volante-row').forEach(row => {
    row.addEventListener('mouseenter', () => {
      const creador = row.dataset.creador || 'Desconocido';
      const creado = row.dataset.creado || '---';
      const editor = row.dataset.editor || 'Sin cambios';
      const editado = row.dataset.editado || '---';

      tooltip.innerHTML = `
        <strong>Creado por:</strong> ${creador}<br>
        <small>${creado}</small><br><br>
        <strong>Editado por:</strong> ${editor}<br>
        <small>${editado}</small>
      `;
      tooltip.style.display = 'block';
    });

    row.addEventListener('mousemove', e => {
      tooltip.style.left = `${e.pageX + 15}px`;
      tooltip.style.top = `${e.pageY + 15}px`;
    });

    row.addEventListener('mouseleave', () => {
      tooltip.style.display = 'none';
    });
  });
});


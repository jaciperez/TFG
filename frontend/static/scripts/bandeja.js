$(document).ready(function() {
  // Inicializa por primera y única vez
  const table = $('#tabla-volantes').DataTable({
    pageLength: 10,
    autoWidth: false,
    scrollX: true,
    language: {
      search:     "🔎 Buscar:",
      lengthMenu: "Mostrar _MENU_ registros",
      info:       "Mostrando _START_ a _END_ de _TOTAL_ registros",
      paginate: { first: "«", last: "»", next: "›", previous: "‹" }
    }
  });

  // Oculta inicialmente todas las columnas de detalle (a partir de la 10)
  const totalCols = table.columns().count();
  for (let i = 10; i < totalCols; i++) {
    table.column(i).visible(false);
  }

  let detallesVisible = false;
  $('#btn-toggle-cols').on('click', function() {
    detallesVisible = !detallesVisible;
    for (let i = 10; i < totalCols; i++) {
      table.column(i).visible(detallesVisible);
    }
    table.columns.adjust().draw(false);
    if (table.responsive) table.responsive.recalc();
    $(this).text(detallesVisible ? 'Ver menos…' : 'Ver más…');
  });
});

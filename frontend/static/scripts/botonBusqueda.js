$(document).ready(function () {
  const table = $('#tabla-volantes').DataTable();

  // Abrir/cerrar modal
  $('#btn-adv-search').click(() => $('#adv-search-modal').fadeIn());
  $('.close-modal').click(() => $('#adv-search-modal').fadeOut());
  $('#adv-search-modal').click(e => {
    if (e.target.id === 'adv-search-modal') $('#adv-search-modal').fadeOut();
  });

  // Filtro personalizado
  $.fn.dataTable.ext.search.push((settings, data) => {
    if (settings.nTable.id !== 'tabla-volantes') return true;

    const form = $('#adv-search-form');
    const getDateValue = name => new Date(form.find(`[name="${name}"]`).val());
    const isChecked = name => form.find(`input[name="${name}"]`).is(':checked');
    const textValue = name => form.find(`[name="${name}"]`).val().trim().toLowerCase();

    // Índices de columnas
    const idx = {
      Citado_por: 2, Fecha: 3, Hora: 4, Habitacion: 5, Extension: 6,
      Enfermera: 7, Numero: 8, BOX: 9, Diabetes: 10, Renal: 11,
      Alergia_yodo: 12, Cardiopata: 13, Insulina: 14, ADO: 15,
      Antibioticos: 16, Corticoides: 17, Estadificacion: 18,
      Respuesta_a_tto: 19, Control_evolutivo: 20, TOD: 21,
      Planificacion_RT: 22, Re_Estadistificacion: 23,
      Sospecha_Recidiva: 24, Sospecha_Infeccion: 25, PET: 26, TC: 27,
      RMN: 28, Otro4: 29, Cirugia: 30, RadioT: 31, QuimioT: 32,
      InmunoT: 33, Otro: 34, F_FDG: 35, F_Colina: 36, F_FDOPA: 37,
      F_PSMA: 38, Amiloide: 39, Ga_DOTATOC: 40
    };

    const fechaDesde = form.find('input[name="Fecha_desde"]').val();
    const fechaHasta = form.find('input[name="Fecha_hasta"]').val();
    const fechaVolante = new Date(data[idx.Fecha]);

    if (fechaDesde && fechaVolante < new Date(fechaDesde)) return false;
    if (fechaHasta && fechaVolante > new Date(fechaHasta)) return false;

    // Filtros de texto
    for (let campo of ['Citado_por', 'Hora', 'Habitacion', 'Extension', 'Enfermera', 'Numero', 'BOX']) {
      const filtro = textValue(campo);
      if (filtro && !data[idx[campo]].toLowerCase().includes(filtro)) return false;
    }

    // Filtros booleanos por checkbox
    const camposCheck = [
      'Diabetes', 'Renal', 'Alergia_yodo', 'Cardiopata',
      'Insulina', 'ADO', 'Antibioticos', 'Corticoides',
      'Estadificacion', 'Respuesta_a_tto', 'Control_evolutivo', 'TOD',
      'Planificacion_RT', 'Re_Estadistificacion', 'Sospecha_Recidiva', 'Sospecha_Infeccion',
      'F_FDG', 'F_Colina', 'F_FDOPA', 'F_PSMA', 'Amiloide', 'Ga_DOTATOC'
    ];

    for (let campo of camposCheck) {
      if (isChecked(campo) && data[idx[campo]] !== 'Sí') return false;
    }

    // Filtros de fechas individuales (tipo date exacto)
    const camposFecha = ['PET', 'TC', 'RMN', 'Otro4', 'Cirugia', 'RadioT', 'QuimioT', 'InmunoT', 'Otro'];
    for (let campo of camposFecha) {
      const valorInput = form.find(`[name="${campo}"]`).val();
      if (valorInput) {
        const fechaInput = new Date(valorInput).toDateString();
        const fechaTabla = new Date(data[idx[campo]]).toDateString();
        if (fechaInput !== fechaTabla) return false;
      }
    }

    return true;
  });

  // Aplicar filtros
  $('#adv-search-form').submit(e => {
    e.preventDefault();
    table.draw();
    $('#adv-search-modal').fadeOut();
  });

  // Limpiar filtros
  $('#btn-clear-filters').click(() => {
    $('#adv-search-form')[0].reset();
    table.draw();
  });
});
  
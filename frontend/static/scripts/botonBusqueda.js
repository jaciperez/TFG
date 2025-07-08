$(document).ready(function () {
  const table = $('#tabla-volantes').DataTable();


  const data = table.row(0).data();
  data.forEach((value, i) => console.log(`${i}: ${value}`));

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

    const idx = { 
      num_historia: 2, 
      Citado_por: 3, 
      Fecha: 4, 
      Hora: 5,
      Historia_Clinica: 6,
      Adelantar_si_se_puede: 7,
      Dieta_ENDOCARDITIS: 8,
      Habitacion: 9, 
      Extension: 10, 
      Enfermera: 11, 
      Numero: 12, 
      BOX: 13,
      Diabetes: 14, 
      Renal: 15, 
      Alergia_yodo: 16, 
      Cardiopata: 17,
      Insulina: 18, 
      ADO: 19, 
      Antibioticos: 20, 
      Corticoides: 21,
      Estadificacion: 22, 
      Respuesta_a_tto: 23, 
      Control_evolutivo: 24, 
      TOD: 25,
      Planificacion_RT: 26, 
      Re_Estadistificacion: 27, 
      Sospecha_Recidiva: 28, 
      Sospecha_Infeccion: 29,
      PET: 30, 
      TC: 31, 
      RMN: 32, 
      Otro4: 33,
      Cirugia: 34, 
      RadioT: 35, 
      QuimioT: 36, 
      InmunoT: 37, 
      Otro: 38,
      F_FDG: 39, 
      F_Colina: 40, 
      F_FDOPA: 41, 
      F_PSMA: 42, 
      Amiloide: 43, 
      Ga_DOTATOC: 44,
      Respiratorio: 45, 
      Cardiaco: 46, 
      Planificacion: 47, 
      EARL: 48,
      Intravenoso: 49, 
      CyC: 50, 
      Torax: 51, 
      Portal: 52, 
      Vasvular: 53, 
      Otro2: 54, 
      Oral: 55,
      Rutina: 56, 
      RutinaCraneo: 57, 
      Entero: 58, 
      cyc1: 59, 
      Neuro: 60, 
      Endocarditis: 61,
      ColinaPrecoz: 62, 
      ColinaTardia: 63, 
      Paratiroides: 64, 
      y90: 65, 
      lu177: 66, 
      eess: 67,
      adquisicionInicio: 68, 
      adquisicionFinal: 69, 
      tardiaInicio: 70, 
      tardiaFinal: 71,
      Peso: 72, 
      Altura: 73, 
      embarazo_positivo: 74, 
      embarazo_negativo: 75,
      informado_Contraste: 76, 
      FUR: 77, 
      Glucemia_pre_inyeccion: 78, 
      hora1: 79,
      Actrapid: 80, 
      Lorazepan_Diazepan: 81, 
      Suero: 82, 
      otro_texto: 83, 
      DOSIS: 84,
      inyeccion_izq: 85, 
      inyeccion_dcha: 86, 
      Antecubital: 87, 
      Antebrazo: 88,
      Mano: 89, 
      Pie: 90, 
      otro3_texto: 91,
      Radiofarmaco: 92, 
      contraste1: 93, 
      No_administrado_motivo: 94,
      Extravasacion: 95, 
      Reaccion_Alergica: 96, 
      Intrarterial: 97,
      Malestar_general: 98, 
      Sincope: 99, 
      otro1_texto: 100
    };


    const fechaDesde = form.find('input[name="Fecha_desde"]').val();
    const fechaHasta = form.find('input[name="Fecha_hasta"]').val();
    const fechaVolante = new Date(data[idx.Fecha]);

    if (fechaDesde && fechaVolante < new Date(fechaDesde)) return false;
    if (fechaHasta && fechaVolante > new Date(fechaHasta)) return false;

    // Filtros de texto
    for (let campo of ['Citado_por', 'Hora', 'Habitacion', 'Extension', 'Enfermera', 'Numero', 'BOX', 'Otro2', 'informado_Contraste', 'Glucemia_pre_inyeccion', 'hora1', 'otro_texto', 'DOSIS', 'otro3_texto', 'No_administrado_motivo', 'otro1_texto']) {
      const filtro = textValue(campo);
      if (filtro && !data[idx[campo]]?.toLowerCase().includes(filtro)) return false;
    }

    // Filtros booleanos
    const camposCheck = [
      "Diabetes", "Renal", "Alergia_yodo", "Cardiopata",
      "Insulina", "ADO", "Antibioticos", "Corticoides",
      "Estadificacion", "Respuesta_a_tto", "Control_evolutivo", "TOD",
      "Planificacion_RT", "Re_Estadistificacion", "Sospecha_Recidiva", "Sospecha_Infeccion",
      "F_FDG", "F_Colina", "F_FDOPA", "F_PSMA", "Amiloide", "Ga_DOTATOC",
      "Respiratorio", "Cardiaco", "Planificacion", "EARL",
      "Intravenoso", "CyC", "Torax", "Portal", "Vasvular", "Oral",
      "Rutina", "RutinaCraneo", "Entero", "cyc1", "Neuro", "Endocarditis",
      "ColinaPrecoz", "ColinaTardia", "Paratiroides", "y90", "lu177", "eess",
      "embarazo_positivo", "embarazo_negativo", "Actrapid", "Lorazepan_Diazepan", "Suero",
      "inyeccion_izq", "inyeccion_dcha", "Antecubital", "Antebrazo", "Mano", "Pie",
      "Radiofarmaco", "contraste1", "Extravasacion", "Reaccion_Alergica", "Intrarterial",
      "Malestar_general", "Sincope",
      "Adelantar_si_se_puede",
      "Dieta_ENDOCARDITIS"
    ];


    for (let campo of camposCheck) {
      if (isChecked(campo) && data[idx[campo]] !== 'Sí') return false;
    }

    // Filtros de fechas individuales exactas
    const camposFecha = ["PET", "TC", "RMN", "Otro4", "Cirugia", "RadioT", "QuimioT", "InmunoT", "Otro", "FUR"];
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

function generarPDF() {
    console.log("se ha realizado un volante medico")
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    
    // Imagen en Base64

    
    
    const checkboxSize = 3;
        const drawCheckbox = (x, y, checked) => {
            doc.rect(x, y, checkboxSize, checkboxSize);
            if (checked) {
                doc.line(x, y, x + checkboxSize, y + checkboxSize);
                doc.line(x + checkboxSize, y, x, y + checkboxSize);
            }
        };
        

        // Cuadro identificativo para datos del paciente
        doc.setLineWidth(0.2); // Grosor de la línea
        doc.setDrawColor(0, 0, 0); // Color negro
        doc.setLineDashPattern([2, 2], 0); // Línea de 10px, espacio de 5px
        // Dibuja un cuadrado con líneas rayadas
        doc.rect(140, 5, 60, 30); // (x, y, ancho, alto)
        doc.setLineDashPattern([], 0);


        
        doc.saveGraphicsState();

        // Configuramos estilo de la marca de agua
        doc.setFontSize(12);
        doc.setTextColor(200, 200, 200); // Gris claro
        doc.setFont("helvetica", "bold");

        
        doc.text("IDENT. DEL PACIENTE", 149, 29 , { angle: 21 });

        
        doc.restoreGraphicsState();

    



        // Encabezado
        doc.setFont("Verdana", "bold");
        //doc.line(70, 42, 76.5, 42);
        
        //doc.line(136, 42, 142.5, 42);
        doc.text("MEDICINA NUCLEAR", 77, 44);
        doc.setFont("helvetica");
        doc.setFontSize(8);
        doc.text("Citado por: " + document.getElementById("citado").value, 20, 44);

        // Datos de paciente
        doc.setFontSize(10);
        doc.setFont("helvetica", "normal");
        doc.line(10, 56, 200, 56);
        doc.text("FECHA: " + document.getElementById("fecha").value, 10, 60);
        doc.text("HORA: " + document.getElementById("hora").value, 10, 68);
        doc.text("Hab: " + document.getElementById("paciente").value, 55, 60);
        doc.text("BOX: " + document.getElementById("paciente1").value, 175, 60);
        doc.text("Ext: " + document.getElementById("paciente2").value, 55, 68);
        doc.text("Enfermera: " + document.getElementById("paciente3").value, 90, 60);
        doc.text("Nº: " + document.getElementById("paciente4").value, 150, 60);
        doc.setFont("helvetica", "bold");
        doc.line(10, 69, 200, 69);
        doc.text("HISTORIA CLÍNICA: " + document.getElementById("historia").value, 10, 72.5);
        doc.setFont("helvetica", "normal");
        doc.line(10, 73, 42, 73);  // x1, y1, x2, y2
        let dietaChecked = document.getElementById("dieta").checked;
        let adelantarChecked = document.getElementById("adelantar").checked;

        // Define el tamaño más pequeño del checkbox
        const boxSize = 2.5; // Tamaño pequeño del checkbox

        // Dibuja los checkboxes y coloca "✓" si está marcado
        doc.rect(145.5, 70.2, boxSize, boxSize);  // Dibuja el checkbox para dieta
        if (dietaChecked) {
            // Coloca "✓" centrado dentro del checkbox
            doc.text("x", 146, 72.2);  // Ajusta la posición para centrar el "✓"
        }

        doc.rect(145.5, 76.8, boxSize, boxSize);  // Dibuja el checkbox para adelantar
        if (adelantarChecked) {
            // Coloca "✓" centrado dentro del checkbox
            doc.text("x", 146, 78.8);  // Ajusta la posición para centrar el "✓"
        }

        // Agrega las etiquetas al lado de los checkboxes (más centrado)
        doc.text("Dieta ENDOCARDITIS:", 153, 73);  
        doc.text("Adelantar si se puede:", 153, 79);  



        // linea
        doc.line(10, 82, 96, 82);
        
        // Cuadrado para etiqueta de enfermeria

        doc.setLineWidth(0.2); // Grosor de la línea
        doc.setDrawColor(0, 0, 0); // Color negro
        doc.setLineDashPattern([2, 2], 0); // Línea de 10px, espacio de 5px
        // Dibuja un cuadrado con líneas rayadas
        doc.rect(99, 82, 101.5, 56); // (x, y, ancho, alto)
        doc.setLineDashPattern([], 0);


        // Guardamos estado antes de modificar el contexto gráfico
        doc.saveGraphicsState();

        // Configurar estilo de la marca de agua
        doc.setFontSize(14);
        doc.setTextColor(200, 200, 200); // Gris claro
        doc.setFont("helvetica", "bold");

        
        doc.text("REGISTRO DE INFUSIÓN DE FDG", 114, 126, { angle: 23 });

        // Para restaurar estado gráfico para evitar que afecte a otros textos
        doc.restoreGraphicsState();


        
        // Sección de Antecedentes personales
        let yPos = 88;
        doc.setFont("helvetica", "bold");
        doc.text("Antecedentes Personales:", 10, yPos);

        yPos += 4;
        doc.setFont("helvetica", "normal");

        const checkboxes = [
            { id: "diabetes", label: "Diabetes" },
            { id: "renal", label: "I. Renal" },
            { id: "alergia_yodo", label: "Alergia al Yodo" },
            { id: "cardiopata", label: "Cardiópata" },
            { id: "alergias", label: "Alergias" }
        ];

        // Para dibujar checkboxes en 2 filas
        let colIndex = 0;
        const cols = 2;
        const spaceBetween = 50;
        checkboxes.forEach((checkbox) => {
            let xPos = 10 + colIndex * spaceBetween;
            drawCheckbox(xPos, yPos, document.getElementById(checkbox.id)?.checked || false);
            doc.text(checkbox.label, xPos + checkboxSize + 5, yPos + 3);

            colIndex++;
            if (colIndex >= cols) {
                colIndex = 0;
                yPos += checkboxSize + 3; // Nueva fila
            }
        });

        doc.text("T. de alergia: " + document.getElementById("TipoAlergia").value, 10, 112);

        // Otras enfermedades
        yPos += checkboxSize + 5; // Espacio adicional
        doc.text("Otras enfermedades: " + document.getElementById("otrasEnfermedades").value, 10, 117);

        // Sección de Medicación actual
        yPos += 15.5;
        doc.setFont("helvetica", "bold");
        doc.text("Medicación actual", 10, 122);

        doc.setFont("helvetica", "normal");

        const insulina = document.getElementById("insulina").checked;
        const ADO = document.getElementById("ADO").checked;
        const antibioticos = document.getElementById("antibioticos").checked;
        const corticoides = document.getElementById("corticoides").checked;
        
        doc.text("Insulina", 18, 127);
        drawCheckbox(10, 124, insulina);     
        doc.text("ADO", 68, 127);
        drawCheckbox(60, 124, ADO);
        doc.text("Antibióticos", 18, 132);
        drawCheckbox(10, 129, antibioticos);
        doc.text("Corticoides", 68, 132);
        drawCheckbox(60, 129, corticoides);

        yPos += 1;

        // Motivo de exploración
        yPos = 137;
        doc.setFont("helvetica", "bold");
        doc.text("Motivo de exploración", 10, yPos);

        yPos += 3;
        doc.setFont("helvetica", "normal");
        
        const exploraciones = [
            { id: "Estadificación", label: "Estadificación" },
            { id: "Respuesta a tto", label: "Respuesta a tto" },
            { id: "Control evolutivo", label: "Control evolutivo" },
            { id: "TOD", label: "TOD" },
        ];

        xPos = 10;
        exploraciones.forEach((exploracion) => {
            drawCheckbox(xPos, yPos, document.getElementById(exploracion.id).checked || false);
            doc.text(exploracion.label, xPos + checkboxSize + 5, yPos + 3);
            xPos += 50;
        });

        yPos += 2;
        // Exploraciones pt2 
        yPos += 3;
        doc.setFont("helvetica", "normal");

        const exploracionespt2 = [
            { id: "Planificación RT", label: "Planificación RT" },
            { id: "Re-estadificación", label: "Re-estadificación" },
            { id: "Sospecha recidiva", label: "Sospecha recidiva" },
            { id: "Sospecha infección", label: "Sospecha infección" },
        ];
        
        xPos = 10;
        exploracionespt2.forEach((exploracion) => {
            drawCheckbox(xPos, yPos, document.getElementById(exploracion.id).checked || false);
            doc.text(exploracion.label, xPos + checkboxSize + 5, yPos + 3);
            xPos += 50;
        });
        yPos += 15;
        // Estudios previos:

        doc.setFontSize(10);
        doc.setFont("helvetica", "bold");
        doc.text("Estudios previos", 10, 153);
        doc.setFont("helvetica", "normal");
        doc.text("PET: " + document.getElementById("PET").value, 10, 159);
        doc.text("TC: " + document.getElementById("TC").value, 50, 159);
        doc.text("RMN: " + document.getElementById("RMN").value, 85, 159);
        doc.text("Otro: " + document.getElementById("otro4").value, 124, 159);

        // Final de tratamiento previo:
        doc.setFont("helvetica", "bold");
        doc.text("Final de tratamiento previo", 10, 164);

        doc.setFont("helvetica", "normal");
        doc.text("Cirugía: " + document.getElementById("Cirugía").value, 10, 169);
        doc.text("RatioT: " + document.getElementById("RadioT").value, 50, 169);
        doc.text("QuimioT: " + document.getElementById("QuimioT").value, 85, 169);
        doc.text("InmunoT: " + document.getElementById("InmunoT").value, 124, 169);
        doc.text("Otro: " + document.getElementById("Otro").value, 161, 169);

        doc.line(10, 170.5, 200, 170.5);  // x1, y1, x2, y2

        // Sección de ENFERMERÍA

        doc.setFont("helvetica", "italic", "bold");
        doc.text("ENFERMERÍA", 10, 174);
        doc.line(10, 174.5, 34, 174.5);
        
        
        doc.setFont("helvetica", "normal");
        doc.text("Peso: " + (document.getElementById("peso")?.value || ""), 42, 174);
        doc.text("Altura: " + (document.getElementById("altura")?.value || ""), 70, 174);

        
    
        const contrasteTexto = document.getElementById("contraste_texto").value;
        const contrasteCheckbox = document.getElementById("contraste_checkbox").checked;

        const furTexto = document.getElementById("fur_texto").value;
        const furCheckbox = document.getElementById("fur_checkbox").checked;
        

        
        
        doc.text("C. Informado de contraste: " + contrasteTexto, 107, 174);
        drawCheckbox(103, 171, contrasteCheckbox);

        doc.text("FUR: " + furTexto, 14, 181);
        drawCheckbox(10, 178, furCheckbox);

        // Capturamos el estado de los checkboxes
        const testPositivo = document.getElementById("test_positivo").checked;
        const testNegativo = document.getElementById("test_negativo").checked;
        
        doc.setFont("helvetica", "bold");
        doc.text("Test de embarazo:", 70, 181);
        doc.setFont("helvetica", "normal");
        doc.text("POSITIVO /", 107, 181);
        drawCheckbox(103, 178, testPositivo);

        doc.text("NEGATIVO", 132, 181);
        drawCheckbox(128, 178, testNegativo);


        doc.setFont("helvetica", "bold");
        doc.text("Glucemina Pre-Inyección: " + document.getElementById("glucemia pre-inyeccion").value, 10, 187);
        

        doc.setFont("helvetica", "normal");
        doc.text("Hora: " + document.getElementById("hora1").value, 120, 187);

       // Medicamentos
        doc.setFont("helvetica", "normal");

        const actrapid = document.getElementById("actrapid").checked;
        const lorazepan = document.getElementById("lorazepan").checked;     
        const suero = document.getElementById("suero").checked;
        const otroTexto = document.getElementById("otro_texto").value;
        const otroCheckbox = document.getElementById("otro_checkbox").checked;
       

        doc.text("Actrapid", 14, 193);
        drawCheckbox(10, 190, actrapid);

        doc.text("Lorazepan/Diazepan", 39, 193);
        drawCheckbox(35, 190, lorazepan);

        doc.text("Suero", 83, 193);
        drawCheckbox(79, 190, suero);

        doc.text("Otro: " + otroTexto, 102, 193);
        drawCheckbox(98, 190, otroCheckbox);
        



        // Dosis:
        doc.setFont("helvetica", "bold");
        doc.text("DOSIS: " + document.getElementById("dosis").value, 136, 193);
        doc.setFont("helvetica", "normal");

        // Lugar de inyección
        doc.setFont("helvetica", "bold");
        doc.text("Lugar de inyección:", 10, 199);
        doc.setFont("helvetica", "normal");
        const antecubital = document.getElementById("antecubital").checked;
        const antebrazo = document.getElementById("antebrazo").checked;     
        const mano = document.getElementById("mano").checked;
        const pie = document.getElementById("pie").checked;
        //const otro3 = document.getElementById("otro3").checked;
        const otro3Texto = document.getElementById("otro3_texto").value;
        const otro3Checkbox = document.getElementById("otro3_checkbox").checked;

        const izquierda = document.getElementById("izquierda").checked;
        const derecha= document.getElementById("derecha").checked;
        
        doc.text("IZQUIERDA     /", 55, 199);
        drawCheckbox(51, 196, izquierda);

        doc.text("DERECHA", 90, 199);
        drawCheckbox(86, 196, derecha);

        doc.text("Antecubital", 14, 204.5);
        drawCheckbox(10, 201.5, antecubital);

        doc.text("Antebrazo", 39, 204.5);
        drawCheckbox(35, 201.5, antebrazo);

        doc.text("Mano", 65, 204.5);
        drawCheckbox(61, 201.5, mano);

        doc.text("Pie", 83, 204.5);
        drawCheckbox(79, 201.5, pie);
        
        doc.text("Otro: " + otro3Texto, 102, 204.5);
        drawCheckbox(98, 201.5, otro3Checkbox);


        // Incidencia:
        doc.setFont("helvetica", "bold");
        doc.text("Incidencia  (", 10, 210);
        const radiofarmaco = document.getElementById("radiofarmaco").checked;
        const contraste1 = document.getElementById("contraste1").checked;   
        doc.setFont("helvetica", "normal");  
        const administradoTexto = document.getElementById("administrado_texto").value;
        const administradoCheckbox = document.getElementById("administrado_checkbox").checked;
        const extravasacion = document.getElementById("extravasacion").checked;
        const reaccion = document.getElementById("reaccion").checked;
        const intrarterial = document.getElementById("intrarterial").checked;
        const malestar = document.getElementById("malestar").checked;
        const sincope = document.getElementById("sincope").checked;
        const otro1Texto = document.getElementById("otro1_texto").value;
        const otro1Checkbox = document.getElementById("otro1_checkbox").checked;


      
        doc.setFont("helvetica", "bold");
        doc.text("RADIOFARMACO   /", 35, 210);
        drawCheckbox(31, 207, radiofarmaco);

        doc.text("CONTRASTE):",74, 210);
        drawCheckbox(70, 207, contraste1);
        doc.setFont("helvetica", "normal");

        doc.text("No administrativo (motivo): " + administradoTexto, 107, 210);
        drawCheckbox(103, 207, administradoCheckbox);

        doc.text("Extravasación", 35, 216);
        drawCheckbox(31, 213, extravasacion);

        doc.text("Reacción alérgica", 85, 216);
        drawCheckbox(81, 213, reaccion);
        doc.text("Intrarterial", 130, 216);
        drawCheckbox(126, 213, intrarterial);
        doc.text("Malestar general", 35, 220);
        drawCheckbox(31, 217, malestar);
        doc.text("Síncope", 85, 220);
        drawCheckbox(81, 217, sincope);
        doc.text("Otro: " + otro1Texto, 130, 220);
        drawCheckbox(126, 217, otro1Checkbox);                
        doc.line(10, 222, 200, 222);  // x1, y1, x2, y2


        
        // Radiofármaco
        const fdg = document.getElementById("fdg").checked;
        const colina = document.getElementById("colina").checked;
        const fdopa = document.getElementById("fdopa").checked;
        const psma = document.getElementById("psma").checked;
        const amiloide = document.getElementById("amiloide").checked;
        const dotatoc = document.getElementById("dotatoc").checked;
        

        doc.setFont("helvetica", "bold");
        doc.text("Radiofármaco: ", 10, 226);
        doc.text("F-FDG", 40, 226);
        drawCheckbox(36, 223, fdg);     
        doc.text("F Colina", 66, 226);
        drawCheckbox(62, 223, colina);
        doc.text("F-FDOPA", 93, 226);
        drawCheckbox(89, 223, fdopa);
        doc.text("F-PSMA", 119, 226);
        drawCheckbox(115, 223, psma);
        doc.text("B-Amiloide", 145, 226);
        drawCheckbox(141, 223, amiloide);
        doc.text("Ga-DOTATOC", 173, 226);
        drawCheckbox(169, 223, dotatoc);
        doc.line(10, 227.5, 200, 227.5);  // x1, y1, x2, y2

        doc.setFont("helvetica", "italic", "bold");
        doc.text("TÉCNICOS:", 10, 231);
        doc.line(10, 231.6, 29, 231.6);
        
        doc.setFont("helvetica", "italic", "bold");

        // Gated:
        const respiratorio = document.getElementById("respiratorio").checked;
        const cardiaco = document.getElementById("cardiaco").checked;
        const planificacion1 = document.getElementById("planificacion1").checked;
        const earl = document.getElementById("earl").checked;
        

        doc.setFont("helvetica", "bold");
        doc.text("Gated: ", 37, 231);
        doc.setFont("helvetica", "normal");
        doc.text("Respiratorio", 55, 231);
        drawCheckbox(51, 228, respiratorio);     
        doc.text("Cardiaco", 80, 231);
        drawCheckbox(76, 228, cardiaco);

        doc.setFont("helvetica", "bold");
        doc.text("Planificación RT", 120, 231);
        drawCheckbox(116, 228, planificacion1);
        doc.text("EARL", 158, 231);
        drawCheckbox(154, 228, earl);


        // Contraste
        const intravenoso = document.getElementById("intravenoso").checked;
        const cyc1 = document.getElementById("cyc1").checked;
        const torax = document.getElementById("torax").checked;
        const portal = document.getElementById("portal").checked;
        const vascular = document.getElementById("vascular").checked;
        const otro2Texto = document.getElementById("otro2_texto").value;
        const otro2Checkbox = document.getElementById("otro2_checkbox").checked;
        const oral = document.getElementById("oral").checked;
       
        doc.setFont("helvetica", "bold");
        doc.text("Contraste: ", 10, 237);

        doc.setFont("helvetica", "normal");
        doc.text("Intravenoso (", 40, 237);
        drawCheckbox(36, 234, intravenoso);
        doc.text("C y C", 65, 237);
        drawCheckbox(61, 234, cyc1);
        doc.text("Tórax", 81.5, 237);
        drawCheckbox(77.5, 234, torax);
        doc.text("Portal", 98, 237);
        drawCheckbox(94, 234, portal);
        doc.text("Vascular)", 115, 237);
        drawCheckbox(111, 234, vascular);
        doc.text("Otro: " + otro2Texto, 138, 237);
        drawCheckbox(134, 234, otro2Checkbox);
        doc.text("Oral", 178, 237);
        drawCheckbox(174, 234, oral);
        
        // Protocolo

        const rutina = document.getElementById("rutina").checked;
        const rutinaCraneo = document.getElementById("rutinaCraneo").checked;
        const entero = document.getElementById("entero").checked;
        const cyc = document.getElementById("cyc").checked;
        const neuro = document.getElementById("neuro").checked;
        const endocarditis = document.getElementById("endocarditis").checked;
        const colinaPrecoz = document.getElementById("colinaPrecoz").checked;
        const colinaTardia = document.getElementById("colinaTardia").checked;
        const paratiroides= document.getElementById("paratiroides").checked;
        const y90 = document.getElementById("y90").checked;
        const lu177 = document.getElementById("lu177").checked;
        const eess = document.getElementById("eess").checked;
        
        

        doc.setFont("helvetica", "bold");
        doc.text("Protocolo: ", 10, 243);
        doc.setFont("helvetica", "normal");
        doc.text("Rutina", 40, 243);
        drawCheckbox(36, 240, rutina);     
        doc.text("Rutina + Craneo", 72, 243);
        drawCheckbox(68, 240, rutinaCraneo);
        doc.text("C. Entero", 110, 243);
        drawCheckbox(106, 240, entero);
        doc.text("C y C", 138, 243);
        drawCheckbox(134, 240, cyc);
        doc.text("Neuro", 157, 243);
        drawCheckbox(153, 240, neuro);
        doc.text("Endocarditis", 178, 243);
        drawCheckbox(174, 240, endocarditis);
        doc.text("Colina Precoz", 40, 248);
        drawCheckbox(36, 245, colinaPrecoz);     
        doc.text("Colina Tardía R + C", 72, 248);
        drawCheckbox(68, 245, colinaTardia);
        doc.text("Paratiroides", 110, 248);
        drawCheckbox(106, 245, paratiroides);
        doc.text("Y-90", 138, 248);
        drawCheckbox(134, 245, y90);
        doc.text("Lu-177", 157, 248);
        drawCheckbox(153, 245, lu177);
        doc.text("EESS abajo", 178, 248);
        drawCheckbox(174, 245, eess);


        //Horas de adquisiciones

        doc.setFont("helvetica", "bold");
        doc.text("Hora de adquisición: ", 10, 255);
        doc.text("Tardía: "+ document.getElementById("tardia").value, 10, 260);
        doc.setFont("helvetica", "normal");
        doc.text("Inicio: " + document.getElementById("inicio").value, 50, 255);
        doc.text("Final: " + document.getElementById("final").value, 88, 255);

        doc.text("Inicio: " + document.getElementById("inicio1").value, 50, 260);
        doc.text("Final: " + document.getElementById("final1").value, 88 , 260);

        doc.line(10, 262, 200, 262);
        doc.setFont("helvetica", "bold");
        doc.text("OBSERVACIONES: ", 10, 267);
        doc.text("Vacuna  COVID/", 70, 267);
        doc.text("GRIPE",85,272);
        doc.text("Fecha: ", 100, 267);
        doc.text("Fecha: ", 100, 272);
        doc.text("MSI", 145, 267);
        doc.text("MSD", 162, 267);
        doc.text("Traumatismos: ", 10, 272);
        doc.setFont("helvetica", "normal");
        doc.line(10, 277, 200, 277);
        doc.line(30, 278, 180, 278);

        
        // Obtenemos el nombre del archivo en pdf desde el input (el nombre que pongamos)
        const nombreArchivo = document.getElementById("GuardarArchivo").value.trim();
    
        // Validamos que el nombre no esté vacío
        const nombreFinal = nombreArchivo ? nombreArchivo : "documento";

        // Guardamos el PDF con el nombre deseado
        doc.save(nombreFinal + ".pdf");
    }

document.addEventListener('DOMContentLoaded', function () {
  const historiaInput = document.getElementById('historia');
  const errorSpan = document.getElementById('historia-error');
  const nombreSpan = document.getElementById('paciente-nombre');

  historiaInput.addEventListener('input', function () {
    const valor = historiaInput.value.trim();

    if (valor === '') {
      errorSpan.textContent = '';
      nombreSpan.textContent = '';
      return;
    }

    fetch(`/volante/verificar_historia?valor=${encodeURIComponent(valor)}`)
      .then(response => response.json())
      .then(data => {
        if (!data.existe) {
          errorSpan.textContent = '❌ No existe ningún paciente con ese número de historia';
          nombreSpan.textContent = '';
        } else {
          errorSpan.textContent = '';
          nombreSpan.textContent = `👤 ${data.nombre} ${data.apellidos}`;
        }
      })
      .catch(() => {
        errorSpan.textContent = 'Error al verificar número de historia';
        nombreSpan.textContent = '';
      });
  });
});

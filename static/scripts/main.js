function generarPDF() {
    console.log("se ha realizado un volante medico")
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    
    // Imagen en Base64
    const logoBase64 = "data:image/png;base64,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";
    doc.addImage(logoBase64, "PNG", 10, 10, 86, 14);
    
    
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

        
        // Generamos y descargamos el PDF
        // Obtenemos el nombre del archivo en pdf desde el input (el nombre que pongamos)
        const nombreArchivo = document.getElementById("GuardarArchivo").value.trim();
    
        // Validamos que el nombre no esté vacío
        const nombreFinal = nombreArchivo ? nombreArchivo : "documento";

        // Guardamos el PDF con el nombre deseado
        doc.save(nombreFinal + ".pdf");
    }
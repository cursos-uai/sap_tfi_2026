const lessons=[
  {id:"fundamentos",kicker:"Fundamentos",title:"Diseñar para el cambio",summary:"Antes de dibujar clases hay que decidir por qué se divide el sistema y qué cambio intenta aislar cada parte.",theory:{title:"Idea central",text:"Diseñar es descomponer el software, asignar funciones y establecer relaciones. El criterio no es producir muchas partes: es reducir el costo de los cambios sin degradar la integridad conceptual.",concepts:[["Cambio probable","Anticipar qué requisito, algoritmo, dato o tecnología puede variar."],["Secreto del módulo","Cada módulo aísla una decisión de diseño con alta probabilidad de cambio."],["Interfaz estable","Los clientes usan servicios abstractos y no dependen de la implementación."]]},exercises:[
    {type:"choice",q:"Una empresa puede cambiar el proveedor de pagos varias veces. ¿Qué decisión sigue mejor a Parnas?",options:["Incluir condiciones del proveedor en Pedido","Aislar la integración tras una interfaz de pagos","Exponer el SDK del proveedor a todas las clases"],answer:1,why:"El proveedor es un ítem de cambio. Una interfaz estable evita propagar ese cambio."},
    {type:"choice",q:"¿Cuál es el objetivo principal de un buen diseño?",options:["Usar la mayor cantidad posible de clases","Minimizar el costo de cambio y preservar la integridad conceptual","Copiar directamente el modelo funcional"],answer:1,why:"La cantidad de clases no es el criterio; importa la descomposición frente al cambio."}
  ],source:"Apuntes Una Teoría para el Diseño de Software y Diseño de Software, secciones sobre Diseño para el Cambio y DBOI."},
  {id:"cuentas-dboi",kicker:"Caso guiado · DBOI",title:"Una cuenta preparada para cambiar",summary:"Resolvé en clase una regla bancaria cambiante sin contaminar el módulo que administra el saldo. Abrí un acordeón por vez y compará decisiones antes de revelar la propuesta.",theory:{title:"Desafío",text:"Banco Horizonte necesita limitar el total extraído por día. El límite cambia según el paquete comercial y puede desaparecer. La cuenta ya permite depositar, extraer y consultar saldo.",concepts:[["Meta","Aislar la regla que probablemente cambie."],["Restricción","No exponer saldo, contadores ni estructura interna."],["Criterio de éxito","Cambiar la política sin modificar ni volver a verificar la cuenta básica."]]},walkthrough:true,exercises:[
    {type:"choice",q:"¿Cuál es el ítem de cambio principal de esta variante?",options:["La representación interna del saldo","La política que autoriza extracciones diarias","El nombre de la clase CuentaBancaria"],answer:1,why:"El límite, sus excepciones y su posible eliminación forman una política bancaria con alta probabilidad de cambio."},
    {type:"choice",q:"¿Qué diseño permite retirar la política sin tocar el cliente ni la cuenta básica?",options:["Agregar más condicionales a extraer()","Exponer getSaldoInterno() para que el cliente decida","Componer un ControlExtraccion con la cuenta y conservar la misma interfaz"],answer:2,why:"El control oculta la regla, delega las operaciones básicas y mantiene compatible al código cliente."}
  ],source:"Diseño de Software: DBOI, metodología de Parnas, interfaz e implementación. Problemas Resueltos – Diseño: problemas 1 y 3 sobre cajas de ahorro y cuentas corrientes."},
  {id:"dominio",kicker:"ICONIX · Modelo de dominio",title:"Encontrar conceptos, no soluciones",summary:"El modelo de dominio establece el vocabulario conceptual antes de introducir detalles técnicos.",theory:{title:"Regla de trabajo",text:"Extraé conceptos del problema, sus atributos significativos y relaciones. No confundas entidades del dominio con pantallas, controladores o tablas de una tecnología particular.",concepts:[["Concepto","Objeto reconocible del mundo del problema."],["Atributo","Propiedad significativa del concepto."],["Relación","Vínculo semántico con cardinalidad."]]},exercises:[
    {type:"multi",q:"Seleccioná sólo conceptos del dominio de ventas.",options:["Cliente","PedidoVenta","Botón Confirmar","PostgreSQL","Producto"],answer:[0,1,4],why:"Cliente, PedidoVenta y Producto pertenecen al dominio; el botón y PostgreSQL son detalles de solución."},
    {type:"choice",q:"¿Cuál relación expresa mejor el dominio?",options:["PedidoVenta 1 contiene 1..* LíneaPedido","Form llama a SQL","Controlador importa ORM"],answer:0,why:"La primera relación usa conceptos y cardinalidad sin contaminar el modelo conceptual."}
  ],source:"Proceso ICONIX del repositorio: modelo de dominio conceptual y separación entre requerimientos y diseño."},
  {id:"casos",kicker:"ICONIX · Casos de uso",title:"Narrar comportamiento observable",summary:"Los casos de uso conectan objetivos de actores con respuestas del sistema y preparan el análisis de robustez.",theory:{title:"Del objetivo al flujo",text:"Nombrá el caso de uso con un verbo, identificá actor y objetivo, y redactá pasos en voz activa. Usá include para comportamiento obligatorio reutilizado y extend para comportamiento condicional.",concepts:[["Actor","Rol externo que persigue un objetivo."],["include","Subflujo obligatorio compartido."],["extend","Comportamiento opcional bajo condición."]]},exercises:[
    {type:"choice",q:"Enviar el presupuesto por email es opcional. ¿Qué relación corresponde?",options:["include","extend","generalización de actor"],answer:1,why:"El envío aparece sólo si el vendedor decide realizarlo."},
    {type:"sort",q:"Ordená el camino feliz de Crear presupuesto.",items:["El sistema calcula los totales","El vendedor selecciona el cliente","El vendedor guarda el presupuesto","El vendedor agrega productos"],answer:["El vendedor selecciona el cliente","El vendedor agrega productos","El sistema calcula los totales","El vendedor guarda el presupuesto"],why:"El orden conserva causa y efecto y luego podrá trazarse al diagrama de robustez."}
  ],source:"Casos de uso CU-VEN-001 y D-CU-GEN-002 del repositorio SAP-TFI-2026."},
  {id:"robustez",kicker:"ICONIX · Robustez",title:"Separar frontera, control y entidad",summary:"El análisis de robustez verifica que el texto del caso de uso pueda convertirse en colaboraciones de objetos.",theory:{title:"Tres responsabilidades",text:"El actor interactúa con fronteras; las fronteras invocan controles; los controles coordinan entidades. Evitá que la interfaz manipule directamente la persistencia o que una entidad asuma decisiones de presentación.",concepts:[["Boundary","Pantalla, formulario, API o mensaje visible."],["Control","Coordinador de un flujo o regla de aplicación."],["Entity","Concepto persistente con estado del dominio."]]},exercises:[
    {type:"classify",q:"Clasificá cada elemento del flujo Confirmar pedido.",items:[["Botón Confirmar","Boundary"],["action_confirm()","Control"],["sale.order","Entity"]],options:["Boundary","Control","Entity"],why:"La clasificación mantiene separadas interacción, coordinación y estado."},
    {type:"choice",q:"¿Qué interacción revela mayor acoplamiento indebido?",options:["Actor → Formulario","Formulario → Control","Formulario → PostgreSQL"],answer:2,why:"La frontera conoce un detalle de persistencia y saltea el control y las entidades."}
  ],source:"Diagramas D-ROB del repositorio y principio de bajo acoplamiento del apunte Diseño de Software."},
  {id:"secuencia",kicker:"ICONIX · Secuencia",title:"Asignar mensajes en el tiempo",summary:"El diagrama de secuencia refina el flujo de robustez y asigna operaciones concretas a participantes.",theory:{title:"Trazabilidad temporal",text:"Cada mensaje debe derivarse de un paso del caso de uso y de una interacción de robustez. Las alternativas se representan con condiciones explícitas y las operaciones se asignan al objeto que posee la responsabilidad.",concepts:[["Lifeline","Participante que existe durante la interacción."],["Mensaje","Solicitud de un servicio en orden temporal."],["alt / opt","Variación condicional del flujo."]]},exercises:[
    {type:"sort",q:"Ordená los mensajes de Confirmar pedido.",items:["Stock crea picking","Formulario invoca action_confirm()","Control valida pedido","sale.order cambia a sale"],answer:["Formulario invoca action_confirm()","Control valida pedido","sale.order cambia a sale","Stock crea picking"],why:"Primero se recibe la intención, luego se valida y sólo después se modifican entidades."},
    {type:"choice",q:"Si la validación puede fallar, ¿qué fragmento UML corresponde?",options:["loop","alt / else","par"],answer:1,why:"alt / else muestra caminos mutuamente excluyentes: éxito o error."}
  ],source:"Diagramas D-SEC del repositorio y trazabilidad definida por el proceso ICONIX."},
  {id:"clases",kicker:"ICONIX · Diagrama de clases",title:"Construir clases que oculten decisiones",summary:"El modelo de clases asigna datos, operaciones y relaciones sin exponer decisiones que probablemente cambien.",theory:{title:"De Parnas a UML",text:"Una clase no se justifica sólo porque exista un sustantivo: debe reunir una responsabilidad coherente y proteger un secreto. La interfaz pública debe ser pequeña, abstracta e insensible a cambios anticipados.",concepts:[["Alta cohesión","Los elementos internos contribuyen a un único secreto o responsabilidad."],["Bajo acoplamiento","Las clases conocen la menor cantidad necesaria de otras clases."],["Encapsulamiento","Los parámetros y retornos no revelan la representación interna."]]},exercises:[
    {type:"choice",q:"Un catálogo puede pasar de arreglo a base de datos. ¿Cuál interfaz oculta mejor esa decisión?",options:["Producto[] getArray()","Producto buscarPorId(IdProducto id)","Producto get(int posicion)"],answer:1,why:"Buscar por identidad expresa una necesidad del dominio sin exponer arreglo, posición ni capacidad."},
    {type:"builder",q:"Construí un diseño para descuentos variables.",tokens:["Pedido","PoliticaDescuento","BaseDatosDescuento","calcularTotal()","aplicarA(Pedido)","getFila(int)"],answer:["Pedido","PoliticaDescuento","calcularTotal()","aplicarA(Pedido)"],why:"Pedido compone una Política de Descuento mediante servicios del dominio; la tabla y el acceso por fila quedan ocultos."}
  ],source:"Diseño de Software, secciones DBOI, interfaz/implementación, abstracción, encapsulamiento, cohesión/acoplamiento y diseño orientado a objetos."}
];

let lessonIndex=0;
let progress=JSON.parse(localStorage.getItem("iconix-progress")||"{}");
const selections={};

function saveProgress(){localStorage.setItem("iconix-progress",JSON.stringify(progress))}
function allCorrect(lesson){return lesson.exercises.every((_,i)=>progress[`${lesson.id}-${i}`])}
function renderNav(){
  document.querySelector("#lesson-list").innerHTML=lessons.map((lesson,i)=>`<button class="lesson-button ${i===lessonIndex?"active":""} ${allCorrect(lesson)?"done":""}" data-index="${i}"><span>${allCorrect(lesson)?"✓":i+1}</span><strong>${lesson.title}</strong><small>${lesson.kicker.replace("ICONIX · ","")}</small></button>`).join("");
  const completed=lessons.filter(allCorrect).length;
  document.querySelector("#progress-bar").style.width=`${completed/lessons.length*100}%`;
  document.querySelector("#progress-copy").textContent=`${completed} de ${lessons.length} estaciones completadas`;
}
function renderLesson(){
  const lesson=lessons[lessonIndex];
  document.querySelector("#lesson-kicker").textContent=lesson.kicker;document.querySelector("#lesson-title").textContent=lesson.title;document.querySelector("#lesson-summary").textContent=lesson.summary;
  document.querySelector("#lesson-content").innerHTML=`<article class="theory-card"><p class="eyebrow">${lesson.theory.title}</p><p>${lesson.theory.text}</p></article><div class="concept-grid">${lesson.theory.concepts.map(c=>`<article class="concept-card"><b>${c[0]}</b><p>${c[1]}</p></article>`).join("")}</div>${lesson.walkthrough?walkthroughHTML():""}${lesson.exercises.map((e,i)=>exerciseHTML(e,i,lesson.id)).join("")}<p class="source-note"><b>Base conceptual:</b> ${lesson.source} Fuentes: <a href="https://www.fceia.unr.edu.ar/ingsoft/intro-diseno.pdf" target="_blank" rel="noreferrer">Introducción al diseño ↗</a> · <a href="https://www.fceia.unr.edu.ar/ingsoft/diseno-a.pdf" target="_blank" rel="noreferrer">Diseño y ocultamiento de información ↗</a></p>`;
  document.querySelector("#previous-lesson").disabled=lessonIndex===0;document.querySelector("#next-lesson").textContent=lessonIndex===lessons.length-1?"Finalizar ✓":"Siguiente →";
  updateScore();renderNav();
}
function walkthroughHTML(){
  const steps=[
    ["Comprender el problema",`<h4>Consigna para equipos</h4><p>La cuenta comienza con saldo 0. Permite <code>depositar(m)</code>, <code>extraer(m)</code> y <code>saldo()</code>. Banco Horizonte agrega un límite total diario de extracción: hoy es $100.000, pero varía por paquete y regulación.</p><div class="teacher-prompt"><b>Preguntá antes de avanzar:</b> ¿qué tendría que permanecer estable si mañana el límite aumenta, se vuelve mensual o desaparece?</div><div class="deliverables"><div><b>Rol analista</b><br>Subraya requisitos.</div><div><b>Rol diseñador</b><br>Propone módulos.</div><div><b>Rol revisor</b><br>Busca secretos expuestos.</div></div>`],
    ["Detectar los ítems de cambio",`<h4>Trabajo breve · 6 minutos</h4><p>Separá aquello que puede cambiar de aquello que la cuenta siempre debe hacer. Clasificá cada decisión: representación del saldo, regla del límite diario, registro de lo extraído y mensaje visible al usuario.</p><div class="teacher-prompt"><b>Pista:</b> una decisión de implementación y una regla de negocio no deberían quedar unidas sólo porque participan en la misma operación.</div><div class="reveal"><b>Propuesta para discutir:</b> hay al menos dos secretos: (1) cómo se almacena y actualiza el saldo; (2) cómo se autoriza una extracción según la política vigente. El texto del mensaje pertenece a presentación y no a la cuenta.</div>`],
    ["Cuestionar la solución rápida",`<h4>Primera propuesta</h4><pre class="module-code">extraer(Monto m) {
  if (extraidoHoy + m &lt;= limiteDiario)
    actualizarSaldo(m);
}</pre><div class="teacher-prompt"><b>Debate:</b> ¿qué módulos habría que modificar y volver a probar si cambia el período, aparece un paquete premium o se elimina el límite?</div><div class="reveal"><b>Diagnóstico:</b> la cuenta mezcla el manejo del saldo con la política de autorización. Funciona, pero oculta más de un ítem de cambio y obliga a reabrir un módulo estable ante cada variante comercial.</div>`],
    ["Diseñar interfaces estables",`<h4>Versión mínima en 2MIL</h4><pre class="module-code">Module CuentaBancaria
imports Monto
exports depositar(i Monto)
        extraer(i Monto):Resultado
        saldo():Monto

Module ControlExtraccion
imports CuentaBancaria, Monto
exports depositar(i Monto)
        extraer(i Monto):Resultado
        saldo():Monto</pre><div class="teacher-prompt"><b>Pregunta clave:</b> ¿por qué ambos módulos ofrecen la misma interfaz?</div><div class="reveal"><b>Respuesta:</b> el cliente puede usar el control sin conocer el envoltorio. La interfaz expresa operaciones bancarias, no el contador, el período ni el valor del límite.</div>`],
    ["Resolver mediante composición y delegación",`<h4>Responsabilidades</h4><ul><li><b>CuentaBancaria</b> mantiene el saldo y evita extraer más de lo disponible.</li><li><b>ControlExtraccion</b> compone una cuenta, decide si autoriza y delega depósito, extracción y consulta.</li></ul><pre class="module-code">ControlExtraccion.extraer(Monto m) {
  if permite(m) {
    Resultado r = cuenta.extraer(m);
    if r.aceptado then registrarExtraccion(m);
    return r;
  }
  return rechazado("Límite diario superado");
}</pre><div class="reveal"><b>Secreto protegido:</b> el cliente no sabe si la política usa un acumulador, consulta movimientos o llama a un servicio. Si desaparece, deja de componerse el control sin cambiar CuentaBancaria.</div>`],
    ["Verificar con casos observables",`<h4>Pruebas de aceptación del diseño</h4><table class="test-table"><thead><tr><th>Estado</th><th>Acción</th><th>Resultado</th></tr></thead><tbody><tr><td>Saldo $150.000; extraído hoy $0</td><td>Extraer $60.000</td><td>Acepta; saldo $90.000</td></tr><tr><td>Extraído hoy $60.000</td><td>Extraer $50.000</td><td>Rechaza por límite</td></tr><tr><td>Política desactivada</td><td>Extraer $110.000</td><td>Decide sólo CuentaBancaria</td></tr></tbody></table><div class="teacher-prompt"><b>Cierre:</b> pedí que marquen qué pruebas pertenecen a la cuenta y cuáles al control. La separación de pruebas es una señal de separación de secretos.</div>`],
    ["Transferir a una cuenta corriente",`<h4>Desafío de extensión · 8 minutos</h4><p>Agregá una <b>CuentaCorriente</b> que admite saldo negativo hasta un descubierto configurable. ¿Qué decisión merece otro módulo? ¿Qué interfaz común permitiría calcular el saldo total de cuentas distintas?</p><div class="reveal"><b>Orientación:</b> no agregues un campo <code>tipo</code> y condicionales a una cuenta genérica. Separá CajaAhorros y CuentaCorriente; usá una interfaz CuentaBancaria para tratarlas de forma uniforme y aislá la política de descubierto si cambia independientemente.</div>`]
  ];
  return `<section class="guided-case"><header><div><h2>Resolución guiada</h2><p>Secuencia sugerida: experimentar, argumentar, revelar y revisar.</p></div><span class="time-chip">55 minutos</span></header><div class="case-brief"><b>Entregable del equipo</b><p>Mapa de ítems de cambio + interfaces 2MIL + guía breve de módulos + tres casos de prueba. No se pide código ejecutable.</p></div>${steps.map((step,i)=>`<details class="accordion-step"><summary><span class="step-number">${i+1}</span><span>${step[0]}</span></summary><div class="step-body">${step[1]}</div></details>`).join("")}</section>`
}
function exerciseHTML(e,i,id){
  const common=`<header><div><h3>${i+1}. ${e.q}</h3></div><span class="exercise-type">${({choice:"Una respuesta",multi:"Selección múltiple",sort:"Ordenar",classify:"Clasificar",builder:"Construir"})[e.type]}</span></header>`;
  let body="";
  if(e.type==="choice"||e.type==="multi")body=`<div class="options">${e.options.map((o,n)=>`<button class="option" data-option="${n}"><span>${e.type==="multi"?"□":"○"}</span>${o}</button>`).join("")}</div>`;
  if(e.type==="sort")body=`<div class="sort-list">${e.items.map((item,n)=>`<div class="sort-item" data-value="${item}"><i>${n+1}</i><span>${item}</span><div class="sort-controls"><button data-move="up">↑</button><button data-move="down">↓</button></div></div>`).join("")}</div>`;
  if(e.type==="classify")body=`<div class="options">${e.items.map((item,n)=>`<label class="option">${item[0]}<select data-classify="${n}"><option value="">Elegir…</option>${e.options.map(o=>`<option>${o}</option>`).join("")}</select></label>`).join("")}</div>`;
  if(e.type==="builder")body=`<div class="builder"><div class="palette"><h4>Elementos disponibles</h4>${e.tokens.map((t,n)=>`<button class="token" data-token="${n}">${t}</button>`).join("")}</div><div class="canvas"><h4>Tu diagrama</h4><div class="uml-preview" data-preview><p>Elegí clases y operaciones.</p></div></div></div>`;
  return `<article class="exercise-card" data-exercise="${i}" data-type="${e.type}" data-lesson="${id}">${common}${body}<button class="check-button" data-check>Comprobar</button><div class="feedback"></div></article>`
}
function updateScore(){const lesson=lessons[lessonIndex];const score=lesson.exercises.filter((_,i)=>progress[`${lesson.id}-${i}`]).length;document.querySelector("#lesson-score").textContent=`${score} / ${lesson.exercises.length}`}
function checkExercise(card){
  const lesson=lessons[lessonIndex],i=Number(card.dataset.exercise),e=lesson.exercises[i];let correct=false;
  if(e.type==="choice")correct=Number(card.querySelector(".option.selected")?.dataset.option)===e.answer;
  if(e.type==="multi"){const got=[...card.querySelectorAll(".option.selected")].map(x=>Number(x.dataset.option)).sort();correct=JSON.stringify(got)===JSON.stringify(e.answer)}
  if(e.type==="sort")correct=JSON.stringify([...card.querySelectorAll(".sort-item")].map(x=>x.dataset.value))===JSON.stringify(e.answer);
  if(e.type==="classify")correct=[...card.querySelectorAll("select")].every((x,n)=>x.value===e.items[n][1]);
  if(e.type==="builder"){const got=selections[`${lesson.id}-${i}`]||[];correct=e.answer.every(x=>got.includes(x))&&got.every(x=>e.answer.includes(x))}
  const feedback=card.querySelector(".feedback");feedback.className=`feedback visible ${correct?"success":"error"}`;feedback.textContent=`${correct?"✓ Correcto.":"Todavía no."} ${e.why}`;
  progress[`${lesson.id}-${i}`]=correct;saveProgress();updateScore();renderNav();
}
document.querySelector("#lesson-content").addEventListener("click",event=>{
  const card=event.target.closest(".exercise-card");if(!card)return;
  if(event.target.closest("[data-option]")){const option=event.target.closest("[data-option]");if(card.dataset.type==="choice")card.querySelectorAll(".option").forEach(o=>o.classList.remove("selected"));option.classList.toggle("selected")}
  const mover=event.target.closest("[data-move]");if(mover){const row=mover.closest(".sort-item"),sibling=mover.dataset.move==="up"?row.previousElementSibling:row.nextElementSibling;if(sibling)row.parentElement.insertBefore(mover.dataset.move==="up"?row:sibling,mover.dataset.move==="up"?sibling:row)}
  const token=event.target.closest("[data-token]");if(token){const key=`${lessons[lessonIndex].id}-${card.dataset.exercise}`,value=lessons[lessonIndex].exercises[card.dataset.exercise].tokens[token.dataset.token];selections[key]=selections[key]||[];selections[key]=selections[key].includes(value)?selections[key].filter(x=>x!==value):[...selections[key],value];token.classList.toggle("active");card.querySelector("[data-preview]").innerHTML=builderPreview(selections[key])}
  if(event.target.closest("[data-check]"))checkExercise(card);
});
function builderPreview(items){const classes=items.filter(x=>!x.includes("(")&&!x.startsWith("Base"));const ops=items.filter(x=>x.includes("("));if(!items.length)return"<p>Elegí clases y operaciones.</p>";return classes.map((c,i)=>`<div class="uml-box"><strong>${c}</strong><div>${ops[i]||"+ interfaz abstracta"}</div></div>`).join('<div class="relationship">◇── usa ──▷</div>')}
document.querySelector("#lesson-list").addEventListener("click",e=>{const b=e.target.closest("[data-index]");if(b){lessonIndex=Number(b.dataset.index);renderLesson()}});
document.querySelector("#previous-lesson").addEventListener("click",()=>{if(lessonIndex>0){lessonIndex--;renderLesson();scrollTo(0,0)}});
document.querySelector("#next-lesson").addEventListener("click",()=>{if(lessonIndex<lessons.length-1){lessonIndex++;renderLesson();scrollTo(0,0)}else document.querySelector("#completion-dialog").showModal()});
document.querySelector("#reset-progress").addEventListener("click",()=>{progress={};saveProgress();renderLesson()});document.querySelector("#close-dialog").addEventListener("click",()=>document.querySelector("#completion-dialog").close());
renderLesson();

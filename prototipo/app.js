const scenarios = {
  presupuesto: {
    title: "Crear presupuesto", diagram: "D-ROB-VEN-001", state: "BORRADOR",
    actions: [["Guardar", "primary", "save"], ["Enviar por email", "", "email"], ["Cancelar", "", "cancel"]],
    trace: [
      ["Botón Nuevo + formulario", "Crea y actualiza el presupuesto", "sale.order"],
      ["Campos cliente y líneas", "Calcula importes", "res.partner + sale.order.line"],
      ["Botón Enviar por email", "action_quotation_send()", "sale.order + mail.mail"]
    ]
  },
  confirmacion: {
    title: "Confirmar pedido", diagram: "D-ROB-VEN-004", state: "PRESUPUESTO ENVIADO",
    actions: [["Confirmar", "primary", "confirm"], ["Volver al presupuesto", "", "back"]],
    trace: [
      ["Formulario + botón Confirmar", "action_confirm()", "sale.order"],
      ["Mensaje de validación", "_confirmation_error_message()", "sale.order + sale.order.line"],
      ["Resumen de entrega", "_action_confirm()", "stock.picking"],
      ["Opción de factura", "_create_invoices()", "account.move"]
    ]
  },
  reserva: {
    title: "Reservar productos", diagram: "D-ROB-ENT-002", state: "ESPERANDO RESERVA",
    actions: [["Comprobar disponibilidad", "primary", "reserve"], ["Ver reglas", "", "rules"]],
    trace: [
      ["Botón Comprobar disponibilidad", "action_assign()", "stock.picking"],
      ["Tabla de disponibilidad", "Busca y reserva cantidad", "stock.move.line"],
      ["Aviso de faltante", "Ejecuta reabastecimiento", "stock.warehouse.orderpoint + purchase.order"]
    ]
  },
  factura: {
    title: "Crear factura", diagram: "D-ROB-FAC-001", state: "PARA FACTURAR",
    actions: [["Crear factura", "primary", "invoice"], ["Cancelar", "", "cancel"]],
    trace: [
      ["Botón Crear factura", "_create_invoices()", "sale.order"],
      ["Opciones de facturación", "Valida líneas facturables", "sale.order.line"],
      ["Vista previa de datos", "Calcula y crea factura", "account.move + account.move.line + account.tax"]
    ]
  }
};

const money = new Intl.NumberFormat("es-AR", {style:"currency", currency:"ARS", maximumFractionDigits:0});
const lines = [{product:"Notebook Pro 14", qty:2, price:210000, discount:0, tax:"IVA 21%"},{product:"Dock USB-C", qty:3, price:22000, discount:5, tax:"IVA 21%"}];
let activeScenario = "presupuesto";

function renderLines(){
  const body=document.querySelector("#order-lines");
  body.innerHTML=lines.map((line,i)=>`<tr><td>${line.product}</td><td>${line.qty}</td><td>${money.format(line.price)}</td><td>${line.discount}%</td><td>${line.tax}</td><td>${money.format(line.qty*line.price*(1-line.discount/100))}</td></tr>`).join("");
  const untaxed=lines.reduce((sum,line)=>sum+line.qty*line.price*(1-line.discount/100),0);
  document.querySelector("#untaxed").textContent=money.format(untaxed);
  document.querySelector("#tax").textContent=money.format(untaxed*.21);
  document.querySelector("#total").textContent=money.format(untaxed*1.21);
}

function renderScenario(key){
  activeScenario=key; const scenario=scenarios[key];
  document.querySelectorAll(".nav-item").forEach(item=>item.classList.toggle("active",item.dataset.scenario===key));
  document.querySelectorAll(".screen").forEach(screen=>screen.classList.toggle("active",screen.id===`screen-${key}`));
  document.querySelector("#screen-title").textContent=scenario.title;
  document.querySelector("#diagram-id").textContent=scenario.diagram;
  document.querySelector("#record-state").textContent=scenario.state;
  document.querySelector("#primary-actions").innerHTML=scenario.actions.map(([label,kind,action])=>`<button class="${kind}" data-action="${action}">${label}</button>`).join("");
  document.querySelector("#trace-grid").innerHTML=scenario.trace.map(row=>`<article class="trace-row"><div class="trace-cell boundary-cell"><span>Boundary</span><strong>${row[0]}</strong><p>Elemento que ve o utiliza el actor.</p></div><div class="trace-cell control-cell"><span>Control</span><strong>${row[1]}</strong><p>Comportamiento disparado.</p></div><div class="trace-cell entity-cell"><span>Entity</span><strong>${row[2]}</strong><p>Datos consultados o modificados.</p></div></article>`).join("");
  const diagramBase=location.pathname.includes("/prototipo/")?"../diagrams/svg/":"diagrams/svg/";
  document.querySelector("#diagram-link").href=`${diagramBase}${encodeURIComponent(scenario.diagram)}%20${encodeURIComponent("—")}%20${diagramFilename(key)}.svg`;
  log("Pantalla preparada",`Estás explorando ${scenario.diagram}. Usá los botones para simular el flujo.`);
}

function diagramFilename(key){return {presupuesto:"Diagrama%20de%20Robustez:%20Crear%20Presupuesto",confirmacion:"Diagrama%20de%20Robustez:%20Confirmar%20Pedido",reserva:"Diagrama%20de%20Robustez:%20Reservar%20Productos",factura:"Diagrama%20de%20Robustez:%20Crear%20Factura"}[key]}
function log(title,detail){document.querySelector("#event-title").textContent=title;document.querySelector("#event-detail").textContent=detail}

document.querySelector("#scenario-nav").addEventListener("click",event=>{const item=event.target.closest("[data-scenario]");if(item)renderScenario(item.dataset.scenario)});
document.querySelector(".view-switch").addEventListener("click",event=>{const button=event.target.closest("[data-view]");if(!button)return;document.querySelectorAll(".view-switch button").forEach(b=>b.classList.toggle("active",b===button));document.querySelectorAll(".view").forEach(v=>v.classList.toggle("active",v.id===`${button.dataset.view}-view`))});
document.querySelector("#primary-actions").addEventListener("click",event=>{
  const action=event.target.dataset.action;if(!action)return;
  const messages={save:["Presupuesto guardado","Boundary formulario → actualiza entity sale.order."],email:["Correo preparado","Boundary Enviar → action_quotation_send() → mail.mail."],cancel:["Acción cancelada","No se modificaron entidades en esta simulación."],back:["Volver al presupuesto","Navegación hacia view_sale_order_form."],rules:["Reglas consultadas","Control de reabastecimiento → stock.warehouse.orderpoint."],confirm:["Pedido confirmado","action_confirm() cambió sale.order y generó stock.picking."],reserve:["Reserva procesada","action_assign() reservó 2 unidades y detectó disponibilidad parcial."],invoice:["Factura borrador creada","_create_invoices() → account.move + account.move.line."]};
  if(action==="confirm")document.querySelector("#record-state").textContent="PEDIDO CONFIRMADO";
  if(action==="reserve"){document.querySelector("#reserved-a").textContent="2";document.querySelector("#reserved-b").textContent="1";document.querySelector("#reserve-state-a").textContent="Reservado";document.querySelector("#reserve-state-a").className="pill ok";document.querySelector("#reserve-state-b").textContent="Parcial";document.querySelector("#reserve-state-b").className="pill partial";document.querySelector("#record-state").textContent="PARCIALMENTE DISPONIBLE"}
  if(action==="invoice")document.querySelector("#record-state").textContent="FACTURA BORRADOR";
  log(...messages[action]);
});
document.querySelector("#add-line").addEventListener("click",()=>{lines.push({product:"Monitor 27 pulgadas",qty:1,price:185000,discount:0,tax:"IVA 21%"});renderLines();log("Línea agregada","El formulario actualiza sale.order.line y recalcula los importes de sale.order.")});

renderLines();renderScenario(activeScenario);

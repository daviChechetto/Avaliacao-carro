// ════════════════════════════════════════════════════════════════════
// DATA  — espelha exatamente o que a API Flask retorna
// ════════════════════════════════════════════════════════════════════
const CARROS = [
  {
    id: "escort",
    nome: "Ford Escort Ghia 1.6",
    ano: 1987,
    cor: "#e74c3c",
    carroceria: "Hatch",
    combustivel: "Gasolina",
    potencia_g: 74,
    torque_g: 12.6,
    peso_kg: 880,
    vel_max_g: 157,
    acel_g: 12.6,
    porta_malas_l: 305,
    cilindrada_cc: 1597,
    entre_eixos_mm: 2402,
    consumo_cidade_g: 11.5,
    consumo_estrada_g: 16.8,
    consumo_cidade_e: null,
    consumo_estrada_e: null,
  },
  {
    id: "parati",
    nome: "VW Parati 1.0 16V",
    ano: 1999,
    cor: "#f39c12",
    carroceria: "SW/Perua",
    combustivel: "Gasolina",
    potencia_g: 69,
    torque_g: 9.38,
    peso_kg: 995,
    vel_max_g: 161,
    acel_g: 14.9,
    porta_malas_l: 437,
    cilindrada_cc: 999,
    entre_eixos_mm: 2468,
    consumo_cidade_g: null,
    consumo_estrada_g: null,
    consumo_cidade_e: null,
    consumo_estrada_e: null,
  },
  {
    id: "voyage",
    nome: "VW Voyage 1.0 Flex",
    ano: 2009,
    cor: "#3498db",
    carroceria: "Sedan",
    combustivel: "Flex",
    potencia_g: 72,
    torque_g: 9.7,
    peso_kg: 970,
    vel_max_g: 166,
    acel_g: 13.3,
    porta_malas_l: 480,
    cilindrada_cc: 999,
    entre_eixos_mm: 2465,
    consumo_cidade_g: null,
    consumo_estrada_g: null,
    consumo_cidade_e: null,
    consumo_estrada_e: null,
  },
  {
    id: "sandero",
    nome: "Renault Sandero Zen 1.0",
    ano: 2022,
    cor: "#2ecc71",
    carroceria: "Hatch",
    combustivel: "Flex",
    potencia_g: 79,
    torque_g: 10.2,
    peso_kg: 1011,
    vel_max_g: 160,
    acel_g: 13.3,
    porta_malas_l: 320,
    cilindrada_cc: 999,
    entre_eixos_mm: 2590,
    consumo_cidade_g: 9.6,
    consumo_estrada_g: 14.1,
    consumo_cidade_e: 9.5,
    consumo_estrada_e: 14.2,
  },
];

// ── Chart.js defaults ────────────────────────────────────────────────
Chart.defaults.color = "#4e5580";
Chart.defaults.font.family = "'DM Sans', sans-serif";
Chart.defaults.font.size = 12;

const BORDER_COL = "#1c2138";

function hex2rgb(hex, a) {
  const [r, g, b] = [hex.slice(1, 3), hex.slice(3, 5), hex.slice(5, 7)].map(
    (x) => parseInt(x, 16),
  );
  return `rgba(${r},${g},${b},${a})`;
}

// ── Reusable bar chart factory ───────────────────────────────────────
function makeBar(
  id,
  labels,
  datasets,
  { unit = "", yMax = null, horizontal = false, yTitle = null } = {},
) {
  const ctx = document.getElementById(id);
  return new Chart(ctx, {
    type: "bar",
    data: { labels, datasets },
    options: {
      indexAxis: horizontal ? "y" : "x",
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 900, easing: "easeOutQuart" },
      plugins: {
        legend: {
          display: datasets.length > 1,
          labels: { boxWidth: 10, padding: 14, color: "#7a809a" },
        },
        tooltip: {
          backgroundColor: "#0e1220",
          borderColor: BORDER_COL,
          borderWidth: 1,
          padding: 12,
          titleColor: "#dde2f5",
          bodyColor: "#9aa0c0",
          callbacks: {
            label: (c) =>
              ` ${c.dataset.label || ""} ${c.formattedValue}${unit}`.trim(),
          },
        },
      },
      scales: {
        x: {
          grid: { color: BORDER_COL, lineWidth: 0.6 },
          ticks: { color: "#4e5580" },
        },
        y: {
          grid: { color: BORDER_COL, lineWidth: 0.6 },
          ticks: { color: "#4e5580" },
          beginAtZero: true,
          ...(yMax ? { max: yMax } : {}),
          ...(yTitle
            ? {
                title: {
                  display: true,
                  text: yTitle,
                  color: "#4e5580",
                  font: { size: 11 },
                },
              }
            : {}),
        },
      },
    },
  });
}

// ════════════════════════════════════════════════════════════════════
// BUILD UI
// ════════════════════════════════════════════════════════════════════
function buildPills() {
  document.getElementById("pills").innerHTML = CARROS.map(
    (c) => `
    <div class="pill">
      <span class="pdot" style="background:${c.cor}"></span>
      ${c.nome} <span class="pyear">${c.ano}</span>
    </div>
  `,
  ).join("");
}

function buildStatCards() {
  const relPP = CARROS.map((c) => (c.peso_kg / c.potencia_g).toFixed(2));
  const minIdx = relPP.indexOf(Math.min(...relPP.map(Number)));
  document.getElementById("statCards").innerHTML = CARROS.map(
    (c, i) => `
    <div class="sc" data-id="${c.id}" style="--c-escort:#e74c3c;--c-parati:#f39c12;--c-voyage:#3498db;--c-sandero:#2ecc71">
      <span class="sc-name">${c.nome}</span>
      <span class="sc-tag">${c.ano} · ${c.carroceria} · ${c.combustivel}</span>
      <div class="sc-val" style="color:${c.cor}">${c.peso_kg}</div>
      <div class="sc-sub">
        kg &nbsp;·&nbsp; <strong>${relPP[i]}</strong> kg/cv
        ${i === minIdx ? '<span class="winner-badge">★ melhor relação</span>' : ""}
      </div>
    </div>
  `,
  ).join("");
}

function buildConsumoTable() {
  const MAX = 17;
  function cell(v, cor) {
    if (v == null) return '<span class="nd">n/d</span>';
    return `<strong>${v.toFixed(1)}</strong> km/l
      <div class="bar-il" style="width:${((v / MAX) * 100).toFixed(1)}%;
        background:${hex2rgb(cor, 0.35)};border-left:3px solid ${cor}"></div>`;
  }
  const rows = CARROS.map(
    (c) => `
    <tr>
      <td>
        <strong style="color:${c.cor}">${c.nome}</strong>
        <span class="sc-tag" style="display:block">${c.ano}</span>
        <span class="tag tag-${c.combustivel === "Gasolina" ? "g" : c.combustivel === "Flex" ? "f" : "e"}">${c.combustivel}</span>
      </td>
      <td>${cell(c.consumo_cidade_g, "#e74c3c")}</td>
      <td>${cell(c.consumo_estrada_g, "#f39c12")}</td>
      <td>${cell(c.consumo_cidade_e, "#2ecc71")}</td>
      <td>${cell(c.consumo_estrada_e, "#3498db")}</td>
    </tr>`,
  ).join("");
  document.getElementById("consumoTable").innerHTML = `
    <table class="ctable">
      <thead><tr>
        <th>Carro</th><th>Cidade G</th><th>Estrada G</th><th>Cidade E</th><th>Estrada E</th>
      </tr></thead>
      <tbody>${rows}</tbody>
    </table>
    <p style="font-size:11px;color:var(--muted);margin-top:12px;font-family:'DM Mono',monospace">
      G = gasolina &nbsp;·&nbsp; E = etanol &nbsp;·&nbsp; n/d = não disponível nas fontes consultadas
    </p>`;
}

function buildCharts() {
  const L = CARROS.map((c) => `${c.nome} ${c.ano}`);
  const COR = CARROS.map((c) => c.cor);
  const BG = COR.map((c) => hex2rgb(c, 0.28));
  const BD = COR.map((c) => hex2rgb(c, 0.9));

  const dataset = (data) => [
    {
      label: "",
      data,
      backgroundColor: BG,
      borderColor: BD,
      borderWidth: 2,
      borderRadius: 7,
    },
  ];

  // 01 Potência
  makeBar("cPot", L, dataset(CARROS.map((c) => c.potencia_g)), {
    unit: " cv",
    yMax: 95,
  });

  // 02 Torque
  makeBar("cTorq", L, dataset(CARROS.map((c) => c.torque_g)), {
    unit: " kgfm",
    yMax: 16,
  });

  // 03 Relação Peso/Potência
  const rpp = CARROS.map((c) =>
    parseFloat((c.peso_kg / c.potencia_g).toFixed(2)),
  );
  const maxRPP = Math.max(...rpp);
  makeBar(
    "cPP",
    L,
    [
      {
        label: "kg/cv",
        data: rpp,
        backgroundColor: rpp.map((v, i) =>
          hex2rgb(COR[i], 0.15 + 0.7 * (v / maxRPP)),
        ),
        borderColor: BD,
        borderWidth: 2,
        borderRadius: 7,
      },
    ],
    { unit: " kg/cv", yMax: maxRPP * 1.22, yTitle: "← menor é melhor" },
  );

  // 05 Consumo agrupado
  const cCores = ["#e74c3c", "#2ecc71", "#27ae60"];
  const eCores = ["#c0392b", "#1abc9c", "#16a085"];
  const cLabels = [
    "Escort 1987\n(gasolina)",
    "Sandero 2022\n(gasolina)",
    "Sandero 2022\n(etanol)",
  ];
  makeBar(
    "cCons",
    cLabels,
    [
      {
        label: "Cidade (km/l)",
        data: [11.5, 9.6, 9.5],
        backgroundColor: cCores.map((c) => hex2rgb(c, 0.5)),
        borderColor: cCores,
        borderWidth: 2,
        borderRadius: 7,
      },
      {
        label: "Estrada (km/l)",
        data: [16.8, 14.1, 14.2],
        backgroundColor: eCores.map((c) => hex2rgb(c, 0.22)),
        borderColor: eCores,
        borderWidth: 2,
        borderRadius: 7,
      },
    ],
    { unit: " km/l", yMax: 20 },
  );

  // 06 Velocidade máxima
  makeBar("cVel", L, dataset(CARROS.map((c) => c.vel_max_g)), {
    unit: " km/h",
    yMax: 185,
  });

  // 07 Aceleração
  const acel = CARROS.map((c) => c.acel_g);
  const maxA = Math.max(...acel);
  makeBar(
    "cAcel",
    L,
    [
      {
        label: "segundos",
        data: acel,
        backgroundColor: acel.map((v, i) =>
          hex2rgb(COR[i], 0.1 + 0.7 * (v / maxA)),
        ),
        borderColor: BD,
        borderWidth: 2,
        borderRadius: 7,
      },
    ],
    { unit: " s", yMax: maxA * 1.28, yTitle: "← mais rápido" },
  );

  // 08 Porta-malas
  makeBar("cPM", L, dataset(CARROS.map((c) => c.porta_malas_l)), {
    unit: " L",
    yMax: 580,
  });

  // 09 Cilindrada
  makeBar("cCil", L, dataset(CARROS.map((c) => c.cilindrada_cc)), {
    unit: " cc",
    yMax: 1900,
  });

  // 10 Radar
  const CATS = [
    "Potência (cv)",
    "Torque (kgfm)",
    "Vel. Máx (km/h)",
    "Porta-malas (L)",
    "Entre-eixos (mm)",
  ];
  const raw = CARROS.map((c) => [
    c.potencia_g,
    c.torque_g,
    c.vel_max_g,
    c.porta_malas_l,
    c.entre_eixos_mm,
  ]);
  const maxes = CATS.map((_, i) => Math.max(...raw.map((r) => r[i])));
  const norm = raw.map((r) =>
    r.map((v, i) => parseFloat(((v / maxes[i]) * 100).toFixed(1))),
  );

  new Chart(document.getElementById("cRadar"), {
    type: "radar",
    data: {
      labels: CATS,
      datasets: CARROS.map((c, i) => ({
        label: `${c.nome} ${c.ano}`,
        data: norm[i],
        backgroundColor: hex2rgb(c.cor, 0.12),
        borderColor: hex2rgb(c.cor, 0.85),
        borderWidth: 2.5,
        pointBackgroundColor: c.cor,
        pointRadius: 4,
        pointHoverRadius: 7,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 1100, easing: "easeOutQuart" },
      plugins: {
        legend: {
          position: "bottom",
          labels: { boxWidth: 10, padding: 20, color: "#7a809a" },
        },
        tooltip: {
          backgroundColor: "#0e1220",
          borderColor: BORDER_COL,
          borderWidth: 1,
          padding: 12,
          titleColor: "#dde2f5",
          bodyColor: "#9aa0c0",
          callbacks: {
            label: (c) => ` ${c.dataset.label}: ${c.formattedValue}%`,
          },
        },
      },
      scales: {
        r: {
          angleLines: { color: BORDER_COL },
          grid: { color: BORDER_COL },
          pointLabels: { color: "#b0b8d8", font: { size: 12 } },
          ticks: {
            backdropColor: "transparent",
            color: "#4e5580",
            stepSize: 25,
          },
          min: 0,
          max: 100,
        },
      },
    },
  });
}

// ════════════════════════════════════════════════════════════════════
buildPills();
buildStatCards();
buildConsumoTable();
buildCharts();

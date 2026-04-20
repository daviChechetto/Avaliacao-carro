import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Paleta e estilo ────────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#0f1117",
    "axes.facecolor":   "#1a1d2e",
    "axes.edgecolor":   "#3a3d5c",
    "axes.labelcolor":  "#c8cce8",
    "xtick.color":      "#c8cce8",
    "ytick.color":      "#c8cce8",
    "text.color":       "#e8eaf6",
    "grid.color":       "#2a2d45",
    "grid.linestyle":   "--",
    "grid.alpha":       0.6,
    "font.family":      "DejaVu Sans",
})

CARROS  = ["Escort\nGhia 1987", "Parati\n1.0 16V 1999", "Voyage\n1.0 Flex 2009", "Sandero Zen\n1.0 2022"]
LABELS  = ["Escort Ghia 1987", "Parati 1.0 16V 1999", "Voyage 1.0 Flex 2009", "Sandero Zen 1.0 2022"]
ANOS    = [1987, 1999, 2009, 2022]
CORES   = ["#e74c3c", "#f39c12", "#3498db", "#2ecc71"]

# ── Dados ─────────────────────────────────────────────────────────
POTENCIA_G  = [74,  69,  72,  79]   # cv (gasolina)
POTENCIA_E  = [None, None, 76, 82]  # cv (etanol)
TORQUE_G    = [12.6, 9.38, 9.7,  10.2]
TORQUE_E    = [None, None, 10.6, 10.5]
PESO        = [880,  995,  970, 1011]
VEL_MAX_G   = [157, 161, 166, 160]
VEL_MAX_E   = [None, None, 168, 163]
ACEL_G      = [12.6, 14.9, 13.3, 13.3]
ACEL_E      = [None, None, None, 13.0]
CILINDRADA  = [1597, 999, 999, 999]
PORTA_MALAS = [305, 437, 480, 320]
ENTRE_EIXOS = [2402, 2468, 2465, 2590]
COMPRIMENTO = [3969, 4082, 4230, 4070]

# consumo gasolina  cidade / estrada
CONS_CID_G  = [11.5, None, None, 9.6]
CONS_EST_G  = [16.8, None, None, 14.1]
# consumo etanol cidade / estrada
CONS_CID_E  = [None, None, None, 9.5]
CONS_EST_E  = [None, None, None, 14.2]

REL_PESO_POT = [peso / pot for peso, pot in zip(PESO, POTENCIA_G)]  # kg/cv


def barra(ax, vals, titulo, ylabel, cor_list=None, fmt=".1f"):
    x = np.arange(len(CARROS))
    bars = ax.bar(x, vals, color=cor_list or CORES, width=0.55, zorder=3)
    ax.set_xticks(x); ax.set_xticklabels(CARROS, fontsize=8.5)
    ax.set_title(titulo, fontsize=12, fontweight="bold", pad=10, color="#ffffff")
    ax.set_ylabel(ylabel, fontsize=9)
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(vals)*0.01,
                f"{v:{fmt}}", ha="center", va="bottom", fontsize=9, fontweight="bold", color="#ffffff")
    return bars


fig = plt.figure(figsize=(22, 28), facecolor="#0f1117")
fig.suptitle("Comparativo Técnico: 4 Décadas de Carros Populares Brasileiros\n"
             "Escort Ghia 1987  ·  Parati 1.0 1999  ·  Voyage 1.0 2009  ·  Sandero Zen 2022",
             fontsize=15, fontweight="bold", color="#ffffff", y=0.995)

axes = fig.add_gridspec(5, 2, hspace=0.52, wspace=0.32,
                        left=0.07, right=0.96, top=0.97, bottom=0.03)

# ═══════════════════════════════════════════════════════════════════
# 1 ─ Potência (gasolina)
# ═══════════════════════════════════════════════════════════════════
ax1 = fig.add_subplot(axes[0, 0])
barra(ax1, POTENCIA_G, "① Potência Máxima — Gasolina (cv)", "Cavalos (cv)")
ax1.set_ylim(0, max(POTENCIA_G) * 1.20)

# ═══════════════════════════════════════════════════════════════════
# 2 ─ Torque (gasolina)
# ═══════════════════════════════════════════════════════════════════
ax2 = fig.add_subplot(axes[0, 1])
barra(ax2, TORQUE_G, "② Torque Máximo — Gasolina (kgfm)", "Torque (kgfm)")
ax2.set_ylim(0, max(TORQUE_G) * 1.20)

# ═══════════════════════════════════════════════════════════════════
# 3 ─ Relação Peso / Potência  (gasolina)
# ═══════════════════════════════════════════════════════════════════
ax3 = fig.add_subplot(axes[1, 0])
barra(ax3, REL_PESO_POT,
      "③ Relação Peso / Potência — Gasolina (kg/cv)\n"
      "Quanto MENOR, mais leve e potente é o carro",
      "kg por cv", fmt=".2f")
ax3.set_ylim(0, max(REL_PESO_POT) * 1.20)
# destaque: menor = melhor
melhor_idx = int(np.argmin(REL_PESO_POT))
ax3.get_children()[melhor_idx].set_edgecolor("#ffffff")
ax3.get_children()[melhor_idx].set_linewidth(2.5)
ax3.text(melhor_idx, REL_PESO_POT[melhor_idx] + max(REL_PESO_POT)*0.08,
         "★ melhor", ha="center", fontsize=8, color="#f1c40f", fontweight="bold")

# ═══════════════════════════════════════════════════════════════════
# 4 ─ Peso (kg)
# ═══════════════════════════════════════════════════════════════════
ax4 = fig.add_subplot(axes[1, 1])
barra(ax4, PESO, "④ Peso (kg)", "Peso (kg)", fmt=".0f")
ax4.set_ylim(0, max(PESO) * 1.20)

# ═══════════════════════════════════════════════════════════════════
# 5 ─ Consumo combinado   (gráfico agrupado — gasolina e etanol)
# ═══════════════════════════════════════════════════════════════════
ax5 = fig.add_subplot(axes[2, :])   # ocupa as 2 colunas

labels_cons = ["Escort\n1987\n(gasolina)", "Sandero\n2022\n(gasolina)",
               "Sandero\n2022\n(etanol)"]
cid_vals  = [11.5, 9.6, 9.5]
est_vals  = [16.8, 14.1, 14.2]
cores_cid = ["#e74c3c", "#2ecc71", "#27ae60"]
cores_est = ["#c0392b", "#1abc9c", "#16a085"]

x = np.arange(len(labels_cons))
w = 0.35
b1 = ax5.bar(x - w/2, cid_vals, w, label="Cidade (km/l)",  color=cores_cid, zorder=3, alpha=0.92)
b2 = ax5.bar(x + w/2, est_vals, w, label="Estrada (km/l)", color=cores_est, zorder=3, alpha=0.92,
             hatch="///", edgecolor="#0f1117")

for bar, v in zip(list(b1)+list(b2), cid_vals+est_vals):
    ax5.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3,
             f"{v:.1f}", ha="center", va="bottom", fontsize=9.5, fontweight="bold", color="#ffffff")

ax5.set_xticks(x); ax5.set_xticklabels(labels_cons, fontsize=9)
ax5.set_title("⑤ Consumo de Combustível — Cidade vs Estrada (km/l)\n"
              "(apenas modelos com dados INMETRO disponíveis; Parati 1999 e Voyage 2009 sem dados oficiais)",
              fontsize=11, fontweight="bold", pad=10, color="#ffffff")
ax5.set_ylabel("km / litro", fontsize=9)
ax5.yaxis.grid(True, zorder=0); ax5.set_axisbelow(True)
ax5.set_ylim(0, 20)
ax5.legend(fontsize=9, facecolor="#1a1d2e", edgecolor="#3a3d5c", labelcolor="#e8eaf6")

nota = ("⚠ Consumos do Escort 1987 são estimativas da época (não existia INMETRO/Proconve nesse padrão).\n"
        "   Parati 1999 e Voyage 2009 não possuem dados oficiais acessíveis nas fontes consultadas.")
ax5.text(0.5, -0.13, nota, transform=ax5.transAxes, ha="center", fontsize=7.5,
         color="#aaaacc", style="italic")

# ═══════════════════════════════════════════════════════════════════
# 6 ─ Velocidade máxima (gasolina)
# ═══════════════════════════════════════════════════════════════════
ax6 = fig.add_subplot(axes[3, 0])
barra(ax6, VEL_MAX_G, "⑥ Velocidade Máxima — Gasolina (km/h)", "km/h", fmt=".0f")
ax6.set_ylim(0, max(VEL_MAX_G) * 1.20)

# ═══════════════════════════════════════════════════════════════════
# 7 ─ Aceleração 0–100 km/h (gasolina)
# ═══════════════════════════════════════════════════════════════════
ax7 = fig.add_subplot(axes[3, 1])
barra(ax7, ACEL_G,
      "⑦ Aceleração 0–100 km/h — Gasolina (s)\nMENOR = mais rápido",
      "Segundos (s)", fmt=".1f")
ax7.set_ylim(0, max(ACEL_G) * 1.30)
melhor_acel = int(np.argmin(ACEL_G))
ax7.text(melhor_acel, ACEL_G[melhor_acel] + max(ACEL_G)*0.08,
         "★ mais rápido", ha="center", fontsize=8, color="#f1c40f", fontweight="bold")

# ═══════════════════════════════════════════════════════════════════
# 8 ─ Porta-malas (litros)
# ═══════════════════════════════════════════════════════════════════
ax8 = fig.add_subplot(axes[4, 0])
barra(ax8, PORTA_MALAS, "⑧ Volume do Porta-malas (litros)", "Litros (L)", fmt=".0f")
ax8.set_ylim(0, max(PORTA_MALAS) * 1.22)

# ═══════════════════════════════════════════════════════════════════
# 9 ─ Cilindrada (cc)
# ═══════════════════════════════════════════════════════════════════
ax9 = fig.add_subplot(axes[4, 1])
barra(ax9, CILINDRADA, "⑨ Cilindrada do Motor (cc)", "cc", fmt=".0f")
ax9.set_ylim(0, max(CILINDRADA) * 1.22)

# ═══════════════════════════════════════════════════════════════════
# 10 ─ Radar — perfil geral normalizado
# ═══════════════════════════════════════════════════════════════════
# Remove o subplot anterior e substitui por axes polar
# (axes[...] não suporta polar diretamente; usamos add_axes)
ax10_pos = fig.add_subplot(axes[2, 0])   # temporário para pegar bbox
pos = ax10_pos.get_position()
ax10_pos.remove()

ax10 = fig.add_axes([pos.x0 - 0.03, pos.y0 - 0.01,
                     pos.width + 0.06, pos.height + 0.06],
                    projection="polar", facecolor="#1a1d2e")

categorias = ["Potência\n(cv)", "Torque\n(kgfm)", "Vel. Máx\n(km/h)",
              "Porta-malas\n(L)", "Entre-eixos\n(mm)"]
N = len(categorias)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# normaliza cada dimensão 0–1
datasets_raw = [
    [POTENCIA_G[i], TORQUE_G[i], VEL_MAX_G[i], PORTA_MALAS[i], ENTRE_EIXOS[i]]
    for i in range(4)
]
maxs = [max(d[j] for d in datasets_raw) for j in range(N)]
datasets_norm = [[v/m for v, m in zip(d, maxs)] for d in datasets_raw]

for i, (data, cor, label) in enumerate(zip(datasets_norm, CORES, LABELS)):
    values = data + data[:1]
    ax10.plot(angles, values, color=cor, linewidth=2, linestyle="solid")
    ax10.fill(angles, values, color=cor, alpha=0.12)

ax10.set_xticks(angles[:-1])
ax10.set_xticklabels(categorias, fontsize=7.5, color="#c8cce8")
ax10.set_yticks([0.25, 0.5, 0.75, 1.0])
ax10.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=7, color="#888aaa")
ax10.set_title("⑩ Perfil Geral Normalizado\n(radar comparativo)", fontsize=10,
               fontweight="bold", pad=15, color="#ffffff")
ax10.grid(color="#2a2d45", linestyle="--", alpha=0.7)
ax10.spines["polar"].set_color("#3a3d5c")

# legenda do radar
patches = [mpatches.Patch(color=c, label=l, alpha=0.85) for c, l in zip(CORES, LABELS)]
ax10.legend(handles=patches, loc="lower left", bbox_to_anchor=(-0.28, -0.12),
            fontsize=7.5, facecolor="#1a1d2e", edgecolor="#3a3d5c", labelcolor="#e8eaf6")

# ── Salvar ────────────────────────────────────────────────────────
out = "/mnt/user-data/outputs/comparativo_carros.png"
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="#0f1117")
print(f"Salvo em {out}")
plt.close()

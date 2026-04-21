from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="static")

# ── Dados dos carros (mesmos do script Python) ──────────────────────
CARROS = [
    {
        "id": "escort",
        "nome": "Ford Escort Ghia 1.6",
        "ano": 1987,
        "cor": "#e74c3c",
        "carroceria": "Hatch",
        "origem": "Nacional",
        "motor": {
            "cilindrada_cc": 1597,
            "cilindros": "4 em linha",
            "aspiracao": "Natural",
            "alimentacao": "Carburador",
            "codigo": "CHT",
            "valvulas_por_cilindro": 2,
            "taxa_compressao": "9.5:1",
        },
        "combustivel": "Gasolina",
        "potencia_g": 74,
        "potencia_e": None,
        "torque_g": 12.6,
        "torque_e": None,
        "peso_kg": 880,
        "vel_max_g": 157,
        "vel_max_e": None,
        "acel_0_100_g": 12.6,
        "acel_0_100_e": None,
        "consumo_cidade_g": 11.5,
        "consumo_estrada_g": 16.8,
        "consumo_cidade_e": None,
        "consumo_estrada_e": None,
        "porta_malas_l": 305,
        "tanque_l": 48,
        "entre_eixos_mm": 2402,
        "comprimento_mm": 3969,
        "largura_mm": 1640,
        "altura_mm": 1340,
        "cambio": "Manual 5 marchas",
        "tracao": "Dianteira",
        "freio_diant": "Disco",
        "freio_tras": "Tambor",
        "susp_diant": "Independente McPherson",
        "susp_tras": "Independente McPherson",
        "direcao": "Mecânica",
        "pneus": "165/80 R13",
        "cx": 0.38,
    },
    {
        "id": "parati",
        "nome": "VW Parati 1.0 16V",
        "ano": 1999,
        "cor": "#f39c12",
        "carroceria": "SW / Perua",
        "origem": "Nacional",
        "motor": {
            "cilindrada_cc": 999,
            "cilindros": "4 em linha",
            "aspiracao": "Natural",
            "alimentacao": "Injeção multiponto",
            "codigo": None,
            "valvulas_por_cilindro": 4,
            "taxa_compressao": "8.5:1",
        },
        "combustivel": "Gasolina",
        "potencia_g": 69,
        "potencia_e": None,
        "torque_g": 9.38,
        "torque_e": None,
        "peso_kg": 995,
        "vel_max_g": 161,
        "vel_max_e": None,
        "acel_0_100_g": 14.9,
        "acel_0_100_e": None,
        "consumo_cidade_g": None,
        "consumo_estrada_g": None,
        "consumo_cidade_e": None,
        "consumo_estrada_e": None,
        "porta_malas_l": 437,
        "tanque_l": None,
        "entre_eixos_mm": 2468,
        "comprimento_mm": 4082,
        "largura_mm": 1649,
        "altura_mm": 1416,
        "cambio": "Manual 5 marchas",
        "tracao": "Dianteira",
        "freio_diant": "Disco",
        "freio_tras": None,
        "susp_diant": "McPherson c/ barra estabilizadora",
        "susp_tras": "Braços triangulares",
        "direcao": "Mecânica",
        "pneus": "175/70 R13",
        "cx": None,
    },
    {
        "id": "voyage",
        "nome": "VW Voyage 1.0 Flex",
        "ano": 2009,
        "cor": "#3498db",
        "carroceria": "Sedan",
        "origem": "Nacional",
        "motor": {
            "cilindrada_cc": 999,
            "cilindros": "4 em linha",
            "aspiracao": "Natural",
            "alimentacao": "Injeção multiponto",
            "codigo": None,
            "valvulas_por_cilindro": None,
            "taxa_compressao": None,
        },
        "combustivel": "Flex",
        "potencia_g": 72,
        "potencia_e": 76,
        "torque_g": 9.7,
        "torque_e": 10.6,
        "peso_kg": 970,
        "vel_max_g": 166,
        "vel_max_e": 168,
        "acel_0_100_g": 13.3,
        "acel_0_100_e": None,
        "consumo_cidade_g": None,
        "consumo_estrada_g": None,
        "consumo_cidade_e": None,
        "consumo_estrada_e": None,
        "porta_malas_l": 480,
        "tanque_l": 55,
        "entre_eixos_mm": 2465,
        "comprimento_mm": 4230,
        "largura_mm": 1656,
        "altura_mm": 1464,
        "cambio": "Manual 5 marchas",
        "tracao": "Dianteira",
        "freio_diant": "Disco ventilado",
        "freio_tras": None,
        "susp_diant": "McPherson c/ barra estabilizadora",
        "susp_tras": None,
        "direcao": "Mecânica",
        "pneus": None,
        "cx": 0.31,
    },
    {
        "id": "sandero",
        "nome": "Renault Sandero Zen 1.0",
        "ano": 2022,
        "cor": "#2ecc71",
        "carroceria": "Hatch",
        "origem": "Nacional",
        "motor": {
            "cilindrada_cc": 999,
            "cilindros": "3 em linha",
            "aspiracao": "Natural",
            "alimentacao": "Injeção multiponto",
            "codigo": "B4D",
            "valvulas_por_cilindro": None,
            "taxa_compressao": None,
        },
        "combustivel": "Flex",
        "potencia_g": 79,
        "potencia_e": 82,
        "torque_g": 10.2,
        "torque_e": 10.5,
        "peso_kg": 1011,
        "vel_max_g": 160,
        "vel_max_e": 163,
        "acel_0_100_g": 13.3,
        "acel_0_100_e": 13.0,
        "consumo_cidade_g": 9.6,
        "consumo_estrada_g": 14.1,
        "consumo_cidade_e": 9.5,
        "consumo_estrada_e": 14.2,
        "porta_malas_l": 320,
        "tanque_l": 50,
        "entre_eixos_mm": 2590,
        "comprimento_mm": 4070,
        "largura_mm": 1730,
        "altura_mm": 1536,
        "cambio": "Manual 5 marchas",
        "tracao": "Dianteira",
        "freio_diant": "Disco ventilado",
        "freio_tras": "Tambor",
        "susp_diant": "McPherson independente",
        "susp_tras": "Eixo de torção semi-independente",
        "direcao": "Eletro-hidráulica",
        "pneus": None,
        "cx": None,
    },
]


def rel_peso_pot(c):
    return round(c["peso_kg"] / c["potencia_g"], 2)


@app.route("/api/carros")
def api_carros():
    return jsonify(CARROS)


@app.route("/api/graficos")
def api_graficos():
    labels = [f"{c['nome']} {c['ano']}" for c in CARROS]
    cores  = [c["cor"] for c in CARROS]
    return jsonify({
        "labels": labels,
        "cores":  cores,
        "potencia_g":    [c["potencia_g"]    for c in CARROS],
        "potencia_e":    [c["potencia_e"]    for c in CARROS],
        "torque_g":      [c["torque_g"]      for c in CARROS],
        "torque_e":      [c["torque_e"]      for c in CARROS],
        "peso":          [c["peso_kg"]        for c in CARROS],
        "vel_max_g":     [c["vel_max_g"]     for c in CARROS],
        "vel_max_e":     [c["vel_max_e"]     for c in CARROS],
        "acel_g":        [c["acel_0_100_g"]  for c in CARROS],
        "porta_malas":   [c["porta_malas_l"] for c in CARROS],
        "cilindrada":    [c["motor"]["cilindrada_cc"] for c in CARROS],
        "entre_eixos":   [c["entre_eixos_mm"] for c in CARROS],
        "comprimento":   [c["comprimento_mm"] for c in CARROS],
        "rel_peso_pot":  [rel_peso_pot(c)    for c in CARROS],
        "consumo": {
            "labels_ext":    ["Escort 1987\n(gasolina)", "Sandero 2022\n(gasolina)", "Sandero 2022\n(etanol)"],
            "cidade":        [11.5, 9.6, 9.5],
            "estrada":       [16.8, 14.1, 14.2],
            "cores_cidade":  ["#e74c3c", "#2ecc71", "#27ae60"],
            "cores_estrada": ["#c0392b", "#1abc9c", "#16a085"],
        },
        "radar": {
            "categorias": ["Potência (cv)", "Torque (kgfm)", "Vel. Máx (km/h)", "Porta-malas (L)", "Entre-eixos (mm)"],
            "datasets": [
                {
                    "label": f"{c['nome']} {c['ano']}",
                    "cor":   c["cor"],
                    "valores": [c["potencia_g"], c["torque_g"], c["vel_max_g"], c["porta_malas_l"], c["entre_eixos_mm"]],
                }
                for c in CARROS
            ],
        },
    })


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

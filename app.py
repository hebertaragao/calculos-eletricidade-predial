from flask import Flask, request, render_template
import math

app = Flask(__name__)

def fator_potencia(pot_ativa, pot_aparente):
    return pot_ativa / pot_aparente

def angulo_fase(pot_reativa, pot_ativa):
    return math.atan(pot_reativa / pot_ativa)

def corrente_monofasica(pot_ativa, tensao_fn):
    return pot_ativa / tensao_fn

def corrente_trifasica(pot_ativa, tensao_ff):
    return pot_ativa / (math.sqrt(3) * tensao_ff)

def corrente_potencia_aparente(pot_aparente, tensao):
    return pot_aparente / tensao

def corrente_potencia_ativa(pot_ativa, tensao, fator_potencia):
    return pot_ativa / (tensao * fator_potencia)

def corrente_projeto_corrigida(corrente_projeto, fator_correcao_temp, fator_correcao_agrup):
    return corrente_projeto / (fator_correcao_temp * fator_correcao_agrup)

def dimensionamento_queda_tensao(resistividade, comprimento, corrente_projeto, tensao_max, tensao_fn):
    return (resistividade * comprimento * corrente_projeto * 2) / (tensao_max * tensao_fn) * 100

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pot_ativa = float(request.form['pot_ativa'])
        pot_aparente = float(request.form['pot_aparente'])
        pot_reativa = float(request.form['pot_reativa'])
        tensao_fn = float(request.form['tensao_fn'])
        tensao_ff = float(request.form['tensao_ff'])
        fator_correcao_temp = float(request.form['fator_correcao_temp'])
        fator_correcao_agrup = float(request.form['fator_correcao_agrup'])
        comprimento = float(request.form['comprimento'])
        resistividade = float(request.form['resistividade'])
        tensao_max = float(request.form['tensao_max'])

        # Cálculos
        fp = fator_potencia(pot_ativa, pot_aparente)
        ang_fase = math.degrees(angulo_fase(pot_reativa, pot_ativa))
        corrente_mono = corrente_monofasica(pot_ativa, tensao_fn)
        corrente_tri = corrente_trifasica(pot_ativa, tensao_ff)
        corrente_aparente = corrente_potencia_aparente(pot_aparente, tensao_fn)
        corrente_ativa = corrente_potencia_ativa(pot_ativa, tensao_fn, fp)
        corrente_corrigida = corrente_projeto_corrigida(corrente_mono, fator_correcao_temp, fator_correcao_agrup)
        seccao_nominal = dimensionamento_queda_tensao(resistividade, comprimento, corrente_mono, tensao_max, tensao_fn)
        seccao_nominal = math.ceil(seccao_nominal)  # Arredonda para cima

        return render_template('index.html', fp=fp, ang_fase=ang_fase, corrente_mono=corrente_mono,
                               corrente_tri=corrente_tri, corrente_aparente=corrente_aparente,
                               corrente_ativa=corrente_ativa, corrente_corrigida=corrente_corrigida,
                               seccao_nominal=seccao_nominal)

    return render_template('index.html', fp=None, ang_fase=None, corrente_mono=None, corrente_tri=None,
                           corrente_aparente=None, corrente_ativa=None, corrente_corrigida=None,
                           seccao_nominal=None)

if __name__ == '__main__':
    app.run(debug=True)

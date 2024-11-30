import math

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

def main():
    # Solicitação de dados ao usuário
    pot_ativa = float(input("Digite a potência ativa (P) em watts: "))
    pot_aparente = float(input("Digite a potência aparente (S) em VA: "))
    pot_reativa = float(input("Digite a potência reativa (Q) em VAR: "))
    tensao_fn = float(input("Digite a tensão fase-neutro (Vfn) em volts: "))
    tensao_ff = float(input("Digite a tensão fase-fase (Vff) em volts: "))
    fator_correcao_temp = float(input("Digite o fator de correção de temperatura (Fct): "))
    fator_correcao_agrup = float(input("Digite o fator de correção de agrupamento (Fca): "))
    comprimento = float(input("Digite o comprimento do circuito (L) em metros: "))
    resistividade = float(input("Digite a resistividade do condutor (ρ) em Ω mm²/m: "))
    tensao_max = float(input("Digite a máxima queda de tensão admitida (V%) em porcentagem: "))
    
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
    
    # Resultados
    print(f"Fator de potência (FP): {fp}")
    print(f"Ângulo de fase (φ): {ang_fase} graus")
    print(f"Corrente de projeto monofásica (Ib) em A: {corrente_mono}")
    print(f"Corrente de projeto trifásica (Ib) em A: {corrente_tri}")
    print(f"Corrente de potência aparente (S/V) em A: {corrente_aparente}")
    print(f"Corrente de potência ativa (P/V.cosφ) em A: {corrente_ativa}")
    print(f"Corrente de projeto corrigida (Ipc) em A: {corrente_corrigida}")
    print(f"Secção nominal do condutor (S) em mm²: {seccao_nominal}")

if __name__ == "__main__":
    main()

import random


def verificar_clima():
    """Retorna aleatoriamente a condição climática atual."""
    opcoes = ['Ensolarado', 'Nublado', 'Chuvoso']  # possiblidades do tempo
    return random.choice(opcoes)


def rotina_rega(clima, setor):
    """Define se o setor receberá água conforme o clima e o período."""
    # Em dias de sol, só rega pela manhã
    if clima == 'Ensolarado' and setor['periodo'] == 'Manhã':
        return True
    # Em dias nublados, rega ambos os períodos
    if clima == 'Nublado':
        return True
    # Chuva suspende rega
    return False


def verificar_nutrientes(setor):
    """Avalia NPK do solo e sugere ação caso algum nutriente esteja baixo."""
    # Gera valores simulados para Nitrogênio, Fósforo e Potássio
    nitrogenio = random.uniform(0, 50)
    fosforo = random.uniform(0, 20)
    potassio = random.uniform(0, 40)
    nutrientes = {'N': round(nitrogenio, 1), 'P': round(fosforo, 1), 'K': round(potassio, 1)}

    # Parâmetros mínimos ideais de nutrientes
    ideais = {'N': 20.0, 'P': 10.0, 'K': 15.0}
    status = {}

    # Verifica cada nutriente contra o ideal
    for chave, valor in nutrientes.items():
        status[chave] = 'Adequado' if valor >= ideais[chave] else 'Baixo'

    # Se algum nutriente estiver abaixo, sugere fertilizante
    if any(v == 'Baixo' for v in status.values()):
        acao = "Aplicar fertilizante específico para corrigir níveis baixos"
    else:
        acao = "Níveis de nutrientes adequados, não é necessária ação"

    return nutrientes, status, acao


def main():
    # Lista de setores e seus períodos de monitoramento
    setores = [
        {'nome': 'Canteiro de Rosas', 'periodo': 'Manhã'},
        {'nome': 'Horta', 'periodo': 'Tarde'},
        {'nome': 'Árvores Frutíferas', 'periodo': 'Manhã'},
        {'nome': 'Jardim de Flores Silvestres', 'periodo': 'Tarde'},
        {'nome': 'Viveiro de Suculentas', 'periodo': 'Manhã'},
        {'nome': 'Tanque de Plantas Aquáticas', 'periodo': 'Tarde'},
        {'nome': 'Canaletas de Samambaias', 'periodo': 'Manhã'},
    ]

    clima = verificar_clima()
    print(f"Clima atual: {clima}\n")  # informa condição inicial

    acoes = []
    for setor in setores:
        nome = setor['nome']
        if rotina_rega(clima, setor):
            # Ação de rega registrada
            acoes.append(f"Regou '{nome}' no período {setor['periodo']}")
        else:
            # Sempre checa nutrientes se não regar
            nutrientes, status, recomendacao = verificar_nutrientes(setor)
            detalhes = ", ".join(f"{k}:{v}({status[k]})" for k, v in nutrientes.items())
            acoes.append(
                f"{nome}: não regado. NPK => {detalhes}. Ação: {recomendacao}"
            )

    # Impressão do relatório final
    print("=== Relatório de Ações ===")
    for acao in acoes:
        print(acao)

if __name__ == '__main__':
    main()
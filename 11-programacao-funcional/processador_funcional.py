from functools import reduce, partial

transacoes = [
    {"id": "t1", "tipo": "Credito", "valor": 1500.00, "categoria": "Vendas"},
    {"id": "t2", "tipo": "Debito", "valor": 300.00, "categoria": "Fornecedores"},
    {"id": "t3", "tipo": "Credito", "valor": 5000.00, "categoria": "Vendas"},
    {"id": "t4", "tipo": "Credito", "valor": 800.00, "categoria": "Serviços"},
    {"id": "t5", "tipo": "Credito", "valor": 12000.00, "categoria": "Vendas"},
    {"id": "t6", "tipo": "Pix", "valor": 2500.00, "categoria": "Transferencia"},
]

def eh_do_tipo(tipo_desejado, transacao):
    return transacao["tipo"] == tipo_desejado

def calcular_taxa(transacao):
    TAXA_PROCESSAMENTO = 0.025
    valor_taxa = transacao["valor"] * TAXA_PROCESSAMENTO
    
    nova_transacao = transacao.copy()
    nova_transacao["taxa"] = round(valor_taxa, 2)
    return nova_transacao

def formatar_para_relatorio(transacao):
    return (f"ID: {transacao['id']} | "
            f"Valor Bruto: R$ {transacao['valor']:.2f} | "
            f"Taxa: R$ {transacao['taxa']:.2f}")

def calcular_total_recursivo(lista_de_transacoes):
    if not lista_de_transacoes:
        return 0
    else:
        primeira_transacao = lista_de_transacoes[0]
        resto_da_lista = lista_de_transacoes[1:]
        return primeira_transacao["valor"] + calcular_total_recursivo(resto_da_lista)

if __name__ == "__main__":
    print("--- Pipeline de Análise de Transações ---")
    
    eh_transacao_de_credito = partial(eh_do_tipo, "Credito")

    transacoes_de_credito = filter(eh_transacao_de_credito, transacoes)
    transacoes_com_taxa = map(calcular_taxa, transacoes_de_credito)

    lista_final_transacoes = list(transacoes_com_taxa)
    
    relatorio_formatado = map(formatar_para_relatorio, lista_final_transacoes)

    print("\nRelatório de Transações de Crédito:")
    for linha in relatorio_formatado:
        print(linha)

    total_processado = calcular_total_recursivo(lista_final_transacoes)
    print(f"\nValor total bruto das transações processadas: R$ {total_processado:.2f}")
    
    total_com_reduce = reduce(lambda acumulador, transacao: acumulador + transacao["valor"], lista_final_transacoes, 0)
    print(f"Valor total bruto (calculado com reduce): R$ {total_com_reduce:.2f}")